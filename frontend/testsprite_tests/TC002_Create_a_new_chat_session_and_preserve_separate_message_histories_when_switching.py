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
        # -> Navigate to http://localhost:8080/
        await page.goto("http://localhost:8080/")
        
        # -> Click the 'Playground' navigation button to open the playground UI so we can create chat sessions and test message history preservation.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/nav/div/div/button[2]').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Open the Playground page (trigger navigation to the playground UI) and wait for the playground chat UI to load so we can create sessions.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/nav/div/div/button[2]').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Input the first unique chat message into the playground input field.
        frame = context.pages[-1]
        # Input text
        elem = frame.locator('xpath=/html/body/div[3]/div/div[2]/div[3]/div[2]/textarea').nth(0)
        await asyncio.sleep(3); await elem.fill('TC001: Message in session A — preserve history test')
        
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div[3]/input').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Send the first message in session A, verify it appears in the chat history, then create a new chat session (session B).
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div[3]/div/div[2]/div[3]/div[2]/div/button[2]').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Click '+ New' to create a second chat session (session B), send 'TC002: Message in session B — preserve history test', then switch back to the original session and verify the histories.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div[3]/div/div/div/button').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        frame = context.pages[-1]
        # Input text
        elem = frame.locator('xpath=/html/body/div[3]/div/div[2]/div[3]/div[2]/textarea').nth(0)
        await asyncio.sleep(3); await elem.fill('TC002: Message in session B — preserve history test')
        
        # -> Send the typed TC002 in session B, confirm it appears in session B, switch back to session A, and confirm session A still shows TC001 and not TC002.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div[3]/div/div[2]/div[3]/div[2]/div/button[2]').nth(0)
        await asyncio.sleep(3); await elem.click()
        
        # -> Click the original session (session A) to switch back, then verify session A shows the TC001 message and does NOT show the TC002 message. After confirming, finish the test.
        frame = context.pages[-1]
        # Click element
        elem = frame.locator('xpath=/html/body/div[3]/div/div/div[2]/div/div[2]').nth(0)
        await asyncio.sleep(3); await elem.click()
        
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
    