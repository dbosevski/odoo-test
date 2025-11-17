    # ...existing code...


import asyncio
from playwright.async_api import async_playwright

ODOO_URL = "http://localhost:8069/odoo"  # Ändra vid behov
USERNAME = "draganbosevski@gmail.com"  # Din Odoo-e-post
PASSWORD = "Inf01dbo!"  # Ditt Odoo-lösenord
PRODUKTNAMN = "Testprodukten"  # Använd din skapade produkt

async def run():
            # Skapa ny kund
            # (Flytta tillbaka flödet för att skapa kund, order, produkt och bekräfta order)
            # Efter att knapparna har listats, fortsätt med automationen:
            # Klicka på "Ny"-knappen (justera texten om det behövs)
            try:
                await page.click('button:has-text("Ny")')
            except Exception:
                print("Kunde inte klicka på 'Ny'-knappen, kontrollera knapptext!")
            await asyncio.sleep(1)
            # Fyll i kundnamn
            try:
                await page.fill('input[name="name"]', "Testkund Playwright")
            except Exception:
                print("Kunde inte fylla i kundnamn, kontrollera fältets name-attribut!")
            await asyncio.sleep(1)
            # Klicka på "Spara"-knappen (justera texten om det behövs)
            try:
                await page.click('button:has-text("Spara")')
            except Exception:
                print("Kunde inte klicka på 'Spara'-knappen, kontrollera knapptext!")
            await asyncio.sleep(2)

            # Gå till Försäljning
            print("Väntar på Försäljning-ikonen...")
            await page.wait_for_selector('#result_app_2', state='visible', timeout=10000)
            print("Klickar på Försäljning-ikonen!")
            await page.click('#result_app_2')
            await asyncio.sleep(2)

            # Skapa ny offert/order
            try:
                await page.click('button:has-text("New")')
            except Exception:
                print("Kunde inte klicka på 'New'-knappen, kontrollera knapptext!")
            await asyncio.sleep(1)
            try:
                await page.fill('input[name="partner_id"]', "Testkund Playwright")
            except Exception:
                print("Kunde inte fylla i kundnamn i order, kontrollera fältets name-attribut!")
            await asyncio.sleep(1)
            try:
                await page.click('button:has-text("Add a product")')
            except Exception:
                print("Kunde inte klicka på 'Add a product'-knappen, kontrollera knapptext!")
            await asyncio.sleep(1)
            try:
                await page.fill('input[name="product_id"]', PRODUKTNAMN)
            except Exception:
                print("Kunde inte fylla i produktnamn, kontrollera fältets name-attribut!")
            await asyncio.sleep(1)
            try:
                await page.click('button:has-text("Save")')
            except Exception:
                print("Kunde inte klicka på 'Save'-knappen, kontrollera knapptext!")
            await asyncio.sleep(2)

            # Bekräfta order
            try:
                await page.click('button:has-text("Confirm")')
            except Exception:
                print("Kunde inte klicka på 'Confirm'-knappen, kontrollera knapptext!")
            await asyncio.sleep(2)

            # Verifiera att ordern finns
            await page.goto(f"{ODOO_URL}/web#action=sale.action_orders")
            try:
                assert await page.is_visible('text=Testkund Playwright')
                print("Testet lyckades!")
            except Exception:
                print("Kunde inte verifiera att ordern finns!")
            await browser.close()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(ODOO_URL)
        await asyncio.sleep(2)

        # Logga in
        await page.fill('input[name="login"]', USERNAME)
        await page.fill('input[name="password"]', PASSWORD)
        await page.click('button[type="submit"]')
        # Vänta på att app-ikonerna ska bli synliga
        await page.wait_for_selector('[id^="result_app_"]', state='visible', timeout=15000)
        await asyncio.sleep(2)

        # Efter inloggning, lista alla app-element
        app_elements = await page.query_selector_all('[id^="result_app_"]')
        print(f"Hittade {len(app_elements)} app-element:")
        for el in app_elements:
            el_id = await el.get_attribute('id')


            import asyncio
            from playwright.async_api import async_playwright

            ODOO_URL = "http://localhost:8069/odoo"  # Ändra vid behov
            USERNAME = "draganbosevski@gmail.com"  # Din Odoo-e-post
            PASSWORD = "Inf01dbo!"  # Ditt Odoo-lösenord
            PRODUKTNAMN = "Testprodukten"  # Använd din skapade produkt

            async def run():
                async with async_playwright() as p:
                    browser = await p.chromium.launch(headless=False)
                    page = await browser.new_page()
                    await page.goto(ODOO_URL)
                    await asyncio.sleep(2)

                    # Logga in
                    await page.fill('input[name="login"]', USERNAME)
                    await page.fill('input[name="password"]', PASSWORD)
                    await page.click('button[type="submit"]')
                    await page.wait_for_selector('[id^="result_app_"]', state='visible', timeout=15000)
                    await asyncio.sleep(2)

                    # Gå till Kontaktpersoner
                    await page.wait_for_selector('#result_app_1', state='visible', timeout=10000)
                    await page.click('#result_app_1')
                    await asyncio.sleep(2)

                    # Lista och skriv ut alla synliga knappar på Kontakter-sidan
                    kontakt_knappar = await page.query_selector_all('button')
                    print(f"Hittade {len(kontakt_knappar)} knappar på Kontakter-sidan:")
                    for btn in kontakt_knappar:
                        btn_text = await btn.inner_text()
                        btn_visible = await btn.is_visible()
                        print(f"Knapptxt: '{btn_text}', Synlig: {btn_visible}")
                    await asyncio.sleep(2)

                    # Skapa ny kund
                    try:
                        await page.click('button:has-text("Ny")')
                    except Exception:
                        print("Kunde inte klicka på 'Ny'-knappen, kontrollera knapptext!")
                    await asyncio.sleep(1)
                    try:
                        await page.fill('input[name="name"]', "Testkund Playwright")
                    except Exception:
                        print("Kunde inte fylla i kundnamn, kontrollera fältets name-attribut!")
                    await asyncio.sleep(1)
                    try:
                        await page.click('button:has-text("Spara")')
                    except Exception:
                        print("Kunde inte klicka på 'Spara'-knappen, kontrollera knapptext!")
                    await asyncio.sleep(2)

                    # Gå till Försäljning
                    await page.wait_for_selector('#result_app_2', state='visible', timeout=10000)
                    await page.click('#result_app_2')
                    await asyncio.sleep(2)

                    # Skapa ny offert/order
                    try:
                        await page.click('button:has-text("New")')
                    except Exception:
                        print("Kunde inte klicka på 'New'-knappen, kontrollera knapptext!")
                    await asyncio.sleep(1)
                    try:
                        await page.fill('input[name="partner_id"]', "Testkund Playwright")
                    except Exception:
                        print("Kunde inte fylla i kundnamn i order, kontrollera fältets name-attribut!")
                    await asyncio.sleep(1)
                    try:
                        await page.click('button:has-text("Add a product")')
                    except Exception:
                        print("Kunde inte klicka på 'Add a product'-knappen, kontrollera knapptext!")
                    await asyncio.sleep(1)
                    try:
                        await page.fill('input[name="product_id"]', PRODUKTNAMN)
                    except Exception:
                        print("Kunde inte fylla i produktnamn, kontrollera fältets name-attribut!")
                    await asyncio.sleep(1)
                    try:
                        await page.click('button:has-text("Save")')
                    except Exception:
                        print("Kunde inte klicka på 'Save'-knappen, kontrollera knapptext!")
                    await asyncio.sleep(2)

                    # Bekräfta order
                    try:
                        await page.click('button:has-text("Confirm")')
                    except Exception:
                        print("Kunde inte klicka på 'Confirm'-knappen, kontrollera knapptext!")
                    await asyncio.sleep(2)

                    # Verifiera att ordern finns
                    await page.goto(f"{ODOO_URL}/web#action=sale.action_orders")
                    try:
                        assert await page.is_visible('text=Testkund Playwright')
                        print("Testet lyckades!")
                    except Exception:
                        print("Kunde inte verifiera att ordern finns!")
                    await browser.close()

            if __name__ == "__main__":
                asyncio.run(run())
