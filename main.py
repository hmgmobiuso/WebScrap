import scrap

siteUrl = "http://www.fcblhoops.org/Bulletins.asp?MyTeam=926132&org=FCBLHoops.org"

scrapObj = scrap.Scrap(siteUrl)
scrapObj.scrap_urls_from_page()
