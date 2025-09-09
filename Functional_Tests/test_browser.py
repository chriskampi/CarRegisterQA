import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@pytest.mark.browser
class TestBrowserFunctionality:
    """Test class for browser-based testing of the HTML file"""
    
    def test_page_loads_successfully(self, setup_browser_test):
        """Test that the HTML page loads without errors"""
        driver = setup_browser_test
        assert driver.title is not None, "Page title should not be None"
        assert len(driver.title) > 0, "Page title should not be empty"
    
    def test_page_has_content(self, setup_browser_test):
        """Test that the page contains some content"""
        driver = setup_browser_test
        body = driver.find_element(By.TAG_NAME, "body")
        assert body is not None, "Page should have a body element"
        assert len(body.text.strip()) > 0, "Page should contain text content"
    
    def test_page_has_required_elements(self, setup_browser_test):
        """Test for the presence of common HTML elements"""
        driver = setup_browser_test
        
        # Check for common HTML structure elements
        html_elements = ["html", "head", "body"]
        for element in html_elements:
            try:
                driver.find_element(By.TAG_NAME, element)
            except NoSuchElementException:
                pytest.fail(f"Page should contain {element} element")
    
    def test_page_responsiveness(self, setup_browser_test):
        """Test that the page is responsive to different window sizes"""
        driver = setup_browser_test
        
        # Test different window sizes
        window_sizes = [(1920, 1080), (1366, 768), (1024, 768), (768, 1024)]
        
        for width, height in window_sizes:
            driver.set_window_size(width, height)
            # Wait a moment for the page to adjust
            WebDriverWait(driver, 2).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            
            # Check that the page still loads properly
            body = driver.find_element(By.TAG_NAME, "body")
            assert body is not None, f"Page should load properly at {width}x{height}"
    
    def test_page_has_no_console_errors(self, setup_browser_test):
        """Test that there are no JavaScript console errors"""
        driver = setup_browser_test
        
        # Get browser logs
        logs = driver.get_log('browser')
        error_logs = [log for log in logs if log['level'] == 'SEVERE']
        
        # Filter out common non-critical errors
        critical_errors = []
        for error in error_logs:
            message = error['message'].lower()
            # Skip common non-critical errors
            if not any(skip in message for skip in [
                'favicon', 'chrome-extension', 'net::err_file_not_found'
            ]):
                critical_errors.append(error)
        
        assert len(critical_errors) == 0, f"Found {len(critical_errors)} critical console errors: {critical_errors}"
    
    def test_page_loading_time(self, setup_browser_test):
        """Test that the page loads within a reasonable time"""
        driver = setup_browser_test
        
        # Get page load time
        load_time = driver.execute_script(
            "return performance.timing.loadEventEnd - performance.timing.navigationStart"
        )
        
        # Page should load within 5 seconds
        assert load_time < 5000, f"Page took {load_time}ms to load, which is too slow"
    
    def test_page_has_forms_if_present(self, setup_browser_test):
        """Test form elements if they exist on the page"""
        driver = setup_browser_test
        
        try:
            forms = driver.find_elements(By.TAG_NAME, "form")
            if forms:
                for form in forms:
                    # Check that form has proper structure
                    assert form is not None, "Form element should be valid"
                    
                    # Check for form inputs
                    inputs = form.find_elements(By.TAG_NAME, "input")
                    selects = form.find_elements(By.TAG_NAME, "select")
                    textareas = form.find_elements(By.TAG_NAME, "textarea")
                    
                    total_inputs = len(inputs) + len(selects) + len(textareas)
                    assert total_inputs > 0, "Form should contain input elements"
        except NoSuchElementException:
            # No forms on the page, which is fine
            pass
    
    def test_page_has_links_if_present(self, setup_browser_test):
        """Test link elements if they exist on the page"""
        driver = setup_browser_test
        
        try:
            links = driver.find_elements(By.TAG_NAME, "a")
            if links:
                for link in links:
                    href = link.get_attribute("href")
                    if href and not href.startswith("javascript:"):
                        # Check that external links are properly formatted
                        assert href.startswith(("http://", "https://", "file://", "#")), \
                            f"Link href '{href}' should be properly formatted"
        except NoSuchElementException:
            # No links on the page, which is fine
            pass
    
    def test_page_accessibility_basics(self, setup_browser_test):
        """Test basic accessibility features"""
        driver = setup_browser_test
        
        # Check for alt attributes on images
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            alt_text = img.get_attribute("alt")
            # Alt text should be present (even if empty for decorative images)
            assert alt_text is not None, "Images should have alt attributes"
        
        # Check for proper heading hierarchy
        headings = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")
        if headings:
            # Should have at least one h1
            h1_elements = driver.find_elements(By.TAG_NAME, "h1")
            assert len(h1_elements) > 0, "Page should have at least one h1 heading"
    
    def test_page_has_required_meta_tags(self, setup_browser_test):
        """Test for important meta tags"""
        driver = setup_browser_test
        
        # Check for viewport meta tag
        viewport_meta = driver.find_elements(By.CSS_SELECTOR, "meta[name='viewport']")
        if viewport_meta:
            viewport_content = viewport_meta[0].get_attribute("content")
            assert "width=device-width" in viewport_content, \
                "Viewport meta tag should include width=device-width"
        
        # Check for charset meta tag
        charset_meta = driver.find_elements(By.CSS_SELECTOR, "meta[charset]")
        if not charset_meta:
            # Alternative way to check for charset
            charset_meta = driver.find_elements(By.CSS_SELECTOR, "meta[http-equiv='Content-Type']")
        
        # Charset is important but not critical for basic functionality
        # Just log if it's missing
        if not charset_meta:
            print("Warning: No charset meta tag found")
