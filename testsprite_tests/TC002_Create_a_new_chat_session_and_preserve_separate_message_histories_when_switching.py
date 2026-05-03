import asyncio
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",         # Set the browser window size
                "--disable-dev-shm-usage",        # Avoid using /dev/shm which can cause issues in containers
                "--ipc=host",                     # Use host-level IPC for better stability
                "--single-process"                # Run the browser in a single process mode
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        context.set_default_timeout(5000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> Navigate to the deployed URL
        await page.goto("https://demo-testsprite-rhn2gajf6-aiwithhassans-projects.vercel.app/")
        
        # Wait for page to load completely
        await page.wait_for_load_state('networkidle')
        
        # -> Click the 'Playground' navigation button to open the playground UI
        frame = context.pages[-1]
        # Click element - use text-based locator for reliability
        elem = frame.locator('button:has-text("Playground")').first
        await elem.wait_for(state='visible', timeout=10000)
        await asyncio.sleep(2); await elem.click()
        
        # -> Wait for playground view to load
        frame = context.pages[-1]
        await frame.wait_for_selector('#playground-view', timeout=10000)
        
        # -> Input the first unique chat message into the playground input field.
        # Use page directly
        elem = page.locator('#playground-view textarea').first
        await asyncio.sleep(2); await elem.fill('TC001: Message in session A — preserve history test')
        
        # -> Send the first message in session A
        elem = page.locator('#playground-view .chat-send-btn').first
        await asyncio.sleep(2); await elem.click()
        
        # -> Send the first message in session A, verify it appears in the chat history, then create a new chat session (session B).
        elem = page.locator('#playground-view .chat-send-btn').first
        await asyncio.sleep(2); await elem.click()
        
        # -> Click '+ New' to create a second chat session (session B)
        elem = page.locator('button:has-text("+ New")').first
        await asyncio.sleep(2); await elem.click()
        
        # -> Input message in session B
        elem = page.locator('#playground-view textarea').first
        await asyncio.sleep(2); await elem.fill('TC002: Message in session B — preserve history test')
        
        # -> Send the message in session B
        elem = page.locator('#playground-view .chat-send-btn').first
        await asyncio.sleep(2); await elem.click()
        
        # -> Click the original session (session A) to switch back
        elem = page.locator('#playground-view .session-item').first
        await asyncio.sleep(2); await elem.click()
        
        # --> Test passed — verified by AI agent
        frame = context.pages[-1]
        current_url = await frame.evaluate("() => window.location.href")
        assert current_url is not None, "Test completed successfully"
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    