# Flask Server: GET 🌐

**Detta repo innehåller en Flask-server 🖥 som definierar flera routes 🛤 och uteslutande använder GET-metoden.**

När man arbetar med Flask-routes finns det två huvudsakliga sätt att returnera data till klienten: antingen genom att returnera en ren sträng 📜 eller genom att rendera en HTML-mall 📄. Nedan listas de huvudsakliga skillnaderna mellan dessa två metoder:

- **Returnera en sträng**: Genom att returnera en ren sträng från en Flask-route skickas en textbaserad respons direkt till webbläsaren. Denna metod är praktisk för enklare meddelanden eller för att testa en specifik route. Den returnerade strängen visas som den är i webbläsaren utan någon formatering eller styling.

- **Rendera en HTML-mall**: Genom att använda funktionen `render_template` kan ni skicka tillbaka en strukturerad och stylad webbsida som respons. Flask söker automatiskt efter HTML-mallar i en mapp som kallas __*templates*__. Genom att placera dina mallar i denna mapp kan Flask enkelt hitta och rendera dem när `render_template`-funktionen kallas.

Utöver __*templates*__-mappen finns det ofta en annan mapp kallad __*static*__ där statiska filer som CSS, bilder och JavaScript kan lagras. Flask har en inbyggd funktion, `url_for`, som används för att referera till dessa statiska filer. Mappen __*static*__ är viktig, eftersom dessa filer ofta behövs för att korrekt visa sidans innehåll och funktionalitet.

Genom att skilja på mallar och statiska filer blir det lättare att organisera och underhålla koden. Statiska filer, som CSS och JavaScript, ger möjlighet att presentera mer avancerade och interaktiva webbsidor.

## Statiska Routes 🛤

### Renderar HTML-mall 📄:

1. `/` 
   - **Beskrivning**: Denna route renderar `index.html`-mallen.
   - **Metod**: `GET`
   - **Returnerar**: `index.html`-mallen.

2. `/page` 
   - **Beskrivning**: Denna route renderar `page.html`-mallen.
   - **Metod**: `GET`
   - **Returnerar**: `page.html`-mallen.

### Returnerar en sträng 📜:

3. `/hemsida`
   - **Beskrivning**: Denna route visar ett enkelt meddelande.
   - **Metod**: `GET`
   - **Returnerar**: Strängen "Här är min hemsida".

4. `/my/private/page`
   - **Beskrivning**: Denna route informerar om att sidan är privat 🔒.
   - **Metod**: `GET`
   - **Returnerar**: Strängen "This is a private page!".

## Dynamiska Routes 🔄

Dynamiska routes i Flask gör det möjligt att anpassa innehållet baserat på variabler i URL:en. Dessa variabler kan sedan användas i route-funktionen för att generera ett anpassat svar.

Exempel: I route `/user/<username>`, representerar `<username>` en variabel del av URL:en. Om en användare besöker `/user/Alice`, kommer "Alice" att skickas som en parameter till route-funktionen, och Flask kommer automatiskt att generera ett anpassat svar baserat på denna parameter.

Denna funktionalitet är särskilt användbar för att skapa skalbara webbapplikationer där en route kan hantera många olika förfrågningar baserat på den dynamiska delen av URL:en.

### Parameteriserade Routes 📋

#### Returnerar en dynamisk sträng:

5. `/blog/post/<int:post_id>`
   - **Beskrivning**: Visar en specifik bloggpost 📰 baserad på dess ID.
   - **Metod**: `GET`
   - **Returnerar**: Ett meddelande för den specifika bloggposten.

6. `/user/<username>`
   - **Beskrivning**: Hälsar en användare 🙋 baserat på det angivna användarnamnet.
   - **Metod**: `GET`
   - **Returnerar**: Ett meddelande som välkomnar den angivna användaren.

#### Renderar HTML-mall med dynamiskt innehåll:

7. `/profile/<username>`
   - **Beskrivning**: Visar en användares profil 👤.
   - **Metod**: `GET`
   - **Returnerar**: `profile.html`-mallen med en personlig hälsning baserad på det angivna användarnamnet.


## Kör igång Flask-servern 🚀

För att sätta igång Flask-servern, följ nedanstående steg:

1. **Installera Flask**: Om ni inte redan har installerat Flask kan ni enkelt göra det med pip:
   ```
   pip install Flask
   ```

2. **Starta servern**: När ni har installerat Flask, kan ni starta servern med följande kommando:
   ```
   python app.py
   ```

   När servern är igång bör ni se ett meddelande som talar om att den körs på adressen `http://127.0.0.1:8000/`.

3. **Öppna i webbläsaren**: Besök `http://127.0.0.1:8000/` i er webbläsare för att se er Flask-applikation live!


## Förstå URL:er och Routes 🌐

Tänk på en URL som en adress till ett specifikt rum i ett stort hus 🏠. I detta scenario representerar Flask-servern själva huset, och varje route (eller sökväg) du definierar motsvarar ett unikt rum inom detta hus.

När du startar Flask-servern kommer du att se en adress, t.ex. `http://127.0.0.1:8000/`. Denna adress kan betraktas som husets huvudingång 🚪.

- **Besöka `/`-rummet**: För att komma in i huset genom huvudingången (som leder till standardrummet), navigera till:
  ```
  http://127.0.0.1:8000/
  ```

- **Besöka `/page`-rummet**: Om du vill gå till ett annat rum, t.ex. `/page`-rummet, behöver du bara följa en korridor och lägga till `/page` till huvudingången. För att nå detta rum, gå till:
  ```
  http://127.0.0.1:8000/page
  ```

Varje route du definierar i Flask motsvarar ett sådant rum, och för att besöka det behöver du bara följa den angivna sökvägen från huvudingången.

### Strukturen av en Flask Route 🛠

För att bättre förstå hur routes fungerar i Flask, låt oss titta på den generella strukturen:

```
@FLASK_APP.route(ROUTE_PATH)
def ROUTE_FUNCTION():
       
    [Eventuell kod]

    return RESPONSE_CONTENT
```

Här är:

- **FLASK_APP**: Din Flask-applikationsinstans.
- **ROUTE_PATH**: Den specifika sökväg (t.ex. "/page") som används för att nå den funktionen.
- **ROUTE_FUNCTION**: Den funktion som körs när den angivna sökväg besöks.
- **RESPONSE_CONTENT**: Det innehåll som returneras när funktionen körs, vilket kan vara en sträng, en HTML-mall eller något annat.

Som ett exempel, här är hur `/page`-rummet (eller routen) är definierad:

```
@app.route("/page")
def page():

    return render_template("page.html")
```

Genom att förstå denna struktur och hur varje del av en Flask-route fungerar, kan du enkelt navigera och bygga ditt "hus" av webbsidor med Flask.