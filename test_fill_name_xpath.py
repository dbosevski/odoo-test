import asyncio
from playwright.async_api import async_playwright

ODOO_URL = "http://localhost:8069/odoo"
USERNAME = "draganbosevski@gmail.com"
PASSWORD = "Inf01dbo!"

async def run():
            # Fyll i e-postfältet
            try:
                await page.fill('input[type="email"][id="email_0"]', "test@example.com")
                print("Fyllde i e-post!")
            except Exception as e:
                print(f"Kunde inte fylla i e-post: {e}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(ODOO_URL)
        await asyncio.sleep(2)
        await page.fill('input[name="login"]', USERNAME)
        await page.fill('input[name="password"]', PASSWORD)
        await page.click('button[type="submit"]')
        await page.wait_for_selector('[id^="result_app_"]', state='visible', timeout=15000)
        await asyncio.sleep(2)
        await page.wait_for_selector('#result_app_1', state='visible', timeout=10000)
        await page.click('#result_app_1')
        await asyncio.sleep(2)
        # Klicka på 'Ny'-knappen först
        try:
            await page.click('button:has-text("Ny")')
            print("Klickade på Ny-knappen!")
        except Exception as e:
            print(f"Kunde inte klicka på Ny-knappen: {e}")
        await asyncio.sleep(2)
        # Testa att fylla i företagsnamn med XPath
        try:
            await page.fill('input[placeholder="t.ex. Företaget AB"]', "Testkund Playwright")
            print("Fyllde i företagsnamn!")
        except Exception as e:
            print(f"Kunde inte fylla i företagsnamn: {e}")

        # Fyll i e-postfältet
        try:
            await page.fill('input[type="email"][id="email_0"]', "test@example.com")
            print("Fyllde i e-post!")
        except Exception as e:
            print(f"Kunde inte fylla i e-post: {e}")
        await asyncio.sleep(3)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
