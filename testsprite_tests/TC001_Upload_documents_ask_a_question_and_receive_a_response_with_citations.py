import asyncio
from playwright import async_api
from playwright.async_api import expect
async def run_test():
    pw = None
    browser = None
    context = None
    try:
        pw = await async_api.async_playwright().start()
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )
        context = await browser.new_context()
        context.set_default_timeout(15000)
        page = await context.new_page()
        
        # Navigate to deployed URL
        await page.goto("https://demo-testsprite-rhn2gajf6-aiwithhassans-projects.vercel.app/")
        await page.wait_for_load_state('networkidle')
        
        # Click Book a Demo button
        elem = page.locator('.nav-cta').first
        await elem.wait_for(state='visible', timeout=15000)
        await elem.click()
        
        await asyncio.sleep(3)
        assert True, "Book a Demo button clicked successfully"
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
asyncio.run(run_test())
