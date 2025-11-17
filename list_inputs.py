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
        kontakt_inputs = await page.query_selector_all('input')
        print(f"Hittade {len(kontakt_inputs)} input-fält på Kontakter-sidan:")
        for inp in kontakt_inputs:
            inp_type = await inp.get_attribute('type')
            inp_name = await inp.get_attribute('name')
            inp_placeholder = await inp.get_attribute('placeholder')
            inp_visible = await inp.is_visible()
            print(f"Input: type='{inp_type}', name='{inp_name}', placeholder='{inp_placeholder}', Synlig: {inp_visible}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
