function changeContent(page) {
    var content;
    var heading;
    var content2;
    var heading2;

    if (page === 1) {
        content = "Njegujemo vašu privatnost i cenimo poverenje koje nam pružate. Kada koristite našu platformu, prikupljamo određene podatke radi poboljšanja vašeg iskustva i pružanja boljih usluga. Ovi podaci mogu uključivati informacije o vašoj interakciji sa našom platformom, kao što su pretraživanja, klikovi, vreme provedeno na stranici i slično. <br>Ovi podaci se koriste isključivo u svrhe analize i poboljšanja naše usluge i neće biti deljeni sa trećim stranama bez vaše saglasnosti. Vaša privatnost je naš prioritet, i garantujemo da ćemo pažljivo upravljati svim prikupljenim podacima.";
        heading = "Koje podatke stranica prikuplja?";
        heading2 = "Zašto koristite moje podatke?";
        content2 = "Koristićemo vaše podatke kako bismo poboljšali vaše iskustvo na našoj platformi. Prikupljamo određene informacije o vašem korišćenju kako bismo bolje razumeli naše korisnike i pružili vam personalizovanije usluge. <br>Ovi podaci uključuju informacije o tome koje funkcije našeg sajta koristite, koliko vremena provodite na određenim stranicama, kao i informacije o vašem uređaju, kao što su tip uređaja i lokacija. <br>Ove informacije koristimo isključivo u svrhu analize i poboljšanja naše platforme, kao i pružanja boljih i personalizovanijih usluga našim korisnicima."
    } else if (page === 2) {
        content = "Kako bismo osigurali najbolje moguće iskustvo za sve naše korisnike i očuvali integritet naše platforme, potrebno je da svaki korisnik kreira nalog i prijavi se pre obavljanja bilo kakvih funkcionalnosti na sajtu. <br>Ovo nam omogućava da pružimo personalizovanu uslugu, omogućimo vam pristup svim funkcijama i obezbedimo sigurnost vaših podataka. Kreiranje naloga i prijava su ključni koraci koji osiguravaju da samo ovlašćeni korisnici mogu pristupiti funkcijama naše platforme. <br>To nam omogućava da održavamo visok nivo sigurnosti i zaštite podataka. Vaš nalog će vam omogućiti da pristupite svim funkcijama našeg sajta, uključujući dodavanje sadržaja, interakciju sa drugim korisnicima i još mnogo toga.";
        heading = "Pravila za korisnike";
        heading2 = "*Važno za korisnike!";
        content2 = "Važno je napomenuti da sadržaj koji dodajete na naš sajt mora biti isključivo karaktera koji je naveden. To uključuje, ali nije ograničeno na, muziku, tekst, slike ili bilo koji drugi sadržaj. Svi korisnici su obavezni da poštuju ova pravila i da se suzdrže od dodavanja neprimerenog ili neprikladnog sadržaja. <br>Ukoliko primetite kršenje ovih pravila od strane drugih korisnika, molimo vas da nas odmah obavestite kako bismo preduzeli odgovarajuće mere. Vaša saradnja u održavanju integriteta naše platforme je od suštinskog značaja.";
    } else if (page === 3) {
        content = "Naša politika privatnosti postavlja standarde za zaštitu vaših ličnih podataka. Mi cenimo vašu privatnost i obavezujemo se da ćemo pažljivo čuvati sve informacije koje nam pružite prilikom korišćenja naše platforme. <br>Vaši lični podaci, kao što su ime, adresa, e-mail adresa, telefonski broj i slično, biće korišćeni isključivo u svrhu pružanja i unapređenja naših usluga. Nećemo deliti vaše podatke sa trećim stranama bez vaše saglasnosti, osim u slučajevima kada to zahteva zakon. <br>Pružajući nam svoje podatke, pristajete na našu politiku privatnosti i potvrđujete da ste upoznati sa našim načinom rukovanja ličnim podacima. Vaša privatnost je naš prioritet, i radimo sve što je u našoj moći da je zaštitimo.";
        heading = "Politika privatnosti";
        heading2 = "Zašto je bitna politika privatnosti?";
        content2 = "Naša politika privatnosti je osmišljena kako bi zaštitila vaša prava i privatnost vaših ličnih podataka. Pružajući nam svoje podatke, možete biti sigurni da ćemo ih pažljivo čuvati i koristiti isključivo u skladu sa zakonima i našim internim pravilima. <br>Vaša privatnost je naš prioritet i obavezujemo se da ćemo preduzeti sve potrebne mere kako bismo je zaštitili. Naša politika privatnosti detaljno opisuje kako prikupljamo, koristimo i delimo vaše podatke, kao i koje su vaše opcije u vezi sa tim. <br>Ako imate bilo kakvih pitanja ili nedoumica u vezi sa našom politikom privatnosti, slobodno nas kontaktirajte. Vaša sigurnost i privatnost su od suštinskog značaja za nas i radimo sve što je u našoj moći da ih zaštitimo.";
    }
    document.getElementById('content').innerHTML = content;
    document.getElementById('headingContent').innerText = heading;
    document.getElementById('content2').innerHTML = content2;
    document.getElementById('headingContent2').innerText = heading2;
}