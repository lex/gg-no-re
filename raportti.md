# Ohjelmistuotannon miniprojekti, kevät 2015
### gg ez (Kim Bäckström, Atte Keltanen, Matias Juntunen)

## Sprint 1
Vaatimukset: kirjan lisäys, niiden listaus ja poisto (jos aikaa jää)

Valitsimme toteutusta varten ohjelmointikieleksi Pythonin, jolla on jo ennestään tuttu Flask-mikrokehys helppoa ja nopeaa toteuttamista varten. Tietokannaksi valitsimme MongoDB:n, koska siitä ei kenelläkään ollut ennestään kokemusta.

Valinnat osoittautuivat hyviksi; saimme varsin nopeasti tietokantaoperaatiot toimimaan. Loput ajasta teimme hieman käyttäjäystävällisempää käyttöliittymää. Sitä varten valitsimme suomalaisen Riot.js-kirjaston, josta osalla tiimistä oli jo ennestään kokemusta. Sen avulla saimme toteutettua yksinkertaisen käyttöliittymän pienessä ajassa.

Atte ja Matias päättivät kokeilla toteuttaa projektin pariohjelmoinnilla. Ennakko-odotusten vastaisesti projekti lähti silti hyvin käyntiin, vaikka näppäimistön haltijuudesta tulikin välillä erimielisyyksiä.

Kaikki ohjelmiston tavoitteet saavutettiin ajoissa.

## Sprint 2
Vaatimukset: inproceedings, article

Uusien viitetyyppien lisääminen ohjelmistoon oli helppoa. Loimme vain uudet vastaavat tietokantamallit, ja lisäsimme niille samanlaiset käsittelytoimenpiteet. Tässä vaiheessa toiminnallisuuteen liittyvä boilerplate-koodin monistaminen rupesi arveluttamaan, mutta sen välttäminen olisi toisaalta tehnyt koodista monimutkaisempaa luettavaa. Jos viitetyppejä olisi ollut yhtään enemmän, funktiot olisi varmaan kannattanut siirtää niitä vastaavien luokkien sisään, tai soveltaa samaa funktiota jokaiseen
tyyppiin.

Tämän sprintin aikana saimme myös Jenkinsin pystyyn projektia varten.

Tavoitteet saavutettiin ajoissa, mutta testien toteuttamisen selvittelyyn ei jäänyt enää aikaa.

## Sprint 3
Vaatimukset: testit, uniikki viite (generoitu jos tyhjä), muuta dokumentaatiota

Saimme yksikkötestejä tehtyä huomattavan refaktoroinnin jälkeen. Haastavinta oli löytää muiden tekemiä samaa MongoDB-ajuria käyttäviä testejä, jolloin jouduimme keksimään itse sopivat tavat pystyttää ohjelma ja tietokanta testejä varten.

Generoidussa viitteessä tuli sen verran monta ongelmaa vastaan, ettemme kerenneet sitä tekemään enää määräajassa.

## Post-mortem
Kurssilla esitellyn prosessin noudattaminen tuotti jonkin verran hankaluuksia tiimille. Erityisesti ongelmia tuottivat testit, joiden kirjoittaminen valituilla toteutustekniikoilla olisi vaatinut syvempää perehtymistä. Tässä mielessä projektin toteuttaminen esimerkiksi Springillä olisi ollut parempi idea, koska kaikki tarvittava tieto on tullut jo kurssilla vastaan.

Pariohjelmointikokeilu sujui lopulta melko hyvin. Ongelmana oli lähinnä kommunikaatio, koska ohjelmointikielet eivät sovellu puhuttaviksi ja täten halutun viestin perille saattaminen oli vaikeaa repimättä näppäimistöä toisen käsistä. Lopulta tyydyimme vaihtamaan kirjoittajaa aina silloin, kun jommalla kummalla oli visio ratkaisusta, jota ei osannut selittää kunnolla. Pariohjelmoinnin paras puoli oli ns. kumiankkadebuggaus, joka onnistui automaattisesti toisen henkilön ollessa läsnä.

Jokainen tiimin jäsen oppi enemmän tai vähemmän jotain uutta käytetyistä tekniikoista. Matiakselle Flask oli ennestään jossain määrin tuttu, mutta MongoDB:n ja Riot.js:n kanssa työskentely oli uutta. Atte tunsi Riot.js:ää ja Flaskia jonkin verran jo ennestään, joten hän oppi MongoDB:stä eniten. Kim oppi kaikista käytetyistä tekniikoista jotain uutta.

## TL;DR
### Meni hyvin
* Projektin ominaisuudet saatiin toimimaan
* Pariohjelmointi alkuongelmista huolimatta
* Työnjako

### Meni vähemmän hyvin
* Testaaminen projektin vaatimusten mukaisesti ei onnistunut kovin hyvin (esim. easyB:n puutteesta johtuen)
* JavaScriptiä olisi myös voinut testata, mutta aika ei senkään tutkimiseen enää riittänyt
* Tuntiraportointi
* Koodin dokumentaatio
* Vaaditun prosessin noudattaminen

### Opittiin
* Waffle.io on superkätevä GitHub-integraation ansiosta
* MongoDB:n helppous ja nopeus toteuttaa asioita
* Jenkinsin käyttöä
* Pythonin yksikkötestit ja koodin paloitteleminen niin, että tietokannan testaaminenkin on mahdollista
* Riot.js:n käyttöä


