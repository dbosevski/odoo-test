import asyncio
from playwright.async_api import async_playwright

ODOO_URL = "http://localhost:8069/odoo"
USERNAME = "draganbosevski@gmail.com"
PASSWORD = "Inf01dbo!"

async def run():
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
        # Klicka på Ny
        await page.click('button:has-text("Ny")')
        await asyncio.sleep(2)
        # Fyll i företagsnamn
        await page.fill('input[placeholder="t.ex. Företaget AB"]', "Testkund Playwright")
        # Fyll i e-post
        await page.fill('input[type="email"][id="email_0"]', "test@example.com")
        # Fyll i telefon
        await page.fill('input[type="tel"][id="phone_0"]', "0701234567")
        await asyncio.sleep(5)  # Paus för att se ifyllningen
        # Här kan du lägga till fler fält!
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
