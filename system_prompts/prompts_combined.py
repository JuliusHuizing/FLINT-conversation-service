prompt = """
Ik heb je zojuist een norm gegeven. 
Uiteindelijk willen we act frames genereren op basis van deze norm.
Maar we gaan eerst een paar tussenstappen uitvoeren.

STAP1: 

In het wetboek het wetboek worden normen beschreven. Deze zeggen welk gedrag toelaatbaar is en welk gedrag verplicht is. Er worden dus handelingen besproken die iemand toegestaan is te verrichten en handelingen die iemand moet verrichten. Het kan zo zijn dat een handeling pas verricht mag worden of verricht moet worden als er eerst een andere handeling heeft plaatsgevonden. 
Om het duidelijker te maken zal ik nu een voorbeeld geven. De voorbeeldzin is: 

“De vreemdeling aan wie toegang is geweigerd, dient Nederland onmiddellijk te verlaten, met inachtneming van de aanwijzingen welke hem daartoe door een ambtenaar belast met de grensbewaking, zijn gegeven.” 

Hier moeten twee handelingen uitgehaald worden. 
De eerste is het verlaten van Nederland. Dit is iets wat gedaan moet worden. 
De tweede handeling is het weigeren van toegang. Het verlaten van Nederland moet alleen als eerst de toegang is geweigerd, dus deze handeling moet er ook uitgehaald worden. 

Haal de handelingen zoals hierboven uitgelegd uit de gegeven norm.
Maak een lijst met alle handelingen die je gevonden hebt.


STAP2:

Maak voor elk van deze handelingen een tabel
met de volgende onderdelen:
- ‘Name’: dit is de handeling de in de tekst gevon-
den is - ‘Action’: dit is het werkwoord uit de han-
deling in infinitieve vorm, dus in onbepaalde wijs
- ‘Actor’: dit is degene die de handeling uit mag
voeren of uit moet voeren - ‘Object’: dit is het
lijdend voorwerp, oftewel het object waar de han-
deling op uitgevoerd wordt - ‘Recipient’: dit is de
betrokkene, oftewel degene die de handeling aan-
gaat, oftewel degene die door de handeling wordt
be ̈ınvloed
Om het duidelijker te maken is hier een voor-
beeldzin: “De minister kan de aanvraag tot een
verblijfsvergunning afwijzen.” De handeling is hier
het afwijzen van de aanvraag. Degene die de han-
deling mag uitvoeren is de minister. Het object
is de aanvraag tot een verblijfsvergunning. De be-
trokkene staat niet in deze zin, maar het is duidelijk
dat het degene is die de aanvraag heeft gedaan.
Als een onderdeel niet duidelijk in de tekst staat,
zet dan dit symbool: - in dit deel van de tabel.
Maak voer iedere handeling een eigen tabel.
Als er meerdere handelingen zijn moeten er dus
meerdere tabellen gegeven worden.


STAP3:

Sommige handelingen in het wetboek mogen of
moeten pas verricht worden als er aan bepaalde
voorwaarden wordt voldaan. Dit betekent dat het
rechtmatig uitvoeren van deze handelingen afhangt
van bepaalde omstandigheden of gebeurtenissen.
Dit geldt niet voor alle handelingen die in het wet-
boek beschreven worden.
Een voorbeeld van zin waarin een voorwaarde
staat is: ‘Indien hij volwassen is, mag hij alcohol
kopen’. Hier is ‘hij is volwassen’ een voorwaarde
voor het mogen kopen van alcohol.
Een voorwaarde kan ook negatief zijn. Dat
betekent dat iets alleen mag als iets anders niet
het geval is. Een voorbeeld is: ‘Indien hij niet een
kind is, mag hij alcohol kopen. Hier is ‘niet een
kind zijn’ voorwaarde voor het mogen kopen van
alcohol.

Voeg aan iedere tabel een nieuw onderdeel toe
en zet daarin de voorwaarden waaraan moet zijn
voldaan voordat de handeling uitgevoerd mag wor-
den of uitgevoerd moet worden, zoals hierboven uit-
gelegd. Zet iedere voorwaarde apart tussen deze
haken []. Noem dit onderdeel ‘preconditions’.

"""
