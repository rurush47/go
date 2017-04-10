## Opis działania
Zasadniczo wszystko co was interesuje znajduje się w pliku `flask_api.py`. Żeby odpalić serwer odpalacie skrypt `run_online.py`
Jak checie tylko sobie poklikać żeby sprawdzić zasady to odpalacie `run_offline.py`

Protokół łączenia się z serwerem i gry wygląda następująco:
1. wysyłacie GET'a na `http://adres_serwera:5000/sync`
  * W odpowiedzi dostajecie jsona z:
    * `player_id` - token którym potem będziecie się uwierzytelniać z serwerem
    * `stone_color` - wasz kolor kamieni
2. Żeby pobrać stan gry wysyłacie POST'a na `http://adres_serwera:5000/get_state` z polem formularza `player_id` którego wartość to wasz token
  * W odpowiedzi:
    * `game_state` - lista list gdzie `1` to białe kamienie, `2` to czarne ,a `0` to puste pola. Mapowanie jest w klasie `StoneColor`
    * `is_your_turn` - flaga dająca wam znać czy teraz jest wasz ruch
3. Żeby wysłać ruch który chcecie wykonać wysyłacie POST'a na `http://adres_serwera:5000/send_move` ponownie z polem formularza `player_id` i dwoma dodatkowymi polami formularza `x` i `y` oznajczającymi pole na które chcecie wykonać ruch
  * W odpowiedzi otrzymujecie
    * kod odpowiedzi `200` jeśli ruch ktory wykonaliście jest poprawny
    * kod odpowiedzi `500` jeśli ruch który wykonaliście albo nie jest poprawny albo nie jest wasza tura
    * dodatkowo otrzymujecie zawsze stringa z informacją co się zepsuło

Dodatkowe info:
  * Punkt (0,0) planszy jest w lewym górnym rogu.
  * kod odpowiedzi '418' oznacza problem z autoryzacją albo problem z `player_id` albo już wydano dwa tokeny
  * skrypt `run_online.py` nie ubije się przez Ctrl+C bo pygame stroi fochy, musicie go ubić ręcznie
  * wszelkie uwagi do Mnie i do Olka, jak chcecie coś poprawić w kodzie to dawajcie pull-requesty i nas pingujcie na fejsie

Cała logika gry jest zaimplementowana zgodnie z regułami podanymi [**tutaj**](http://jpolitz.github.io/notes/2012/12/25/go-termination.html) jak chcecie się dokładnie zapytać o coś to męczcie Olka on pisał logikę gry
  
**Ważne** `get_state` nie zwraca histori ruchów w grze co jest istotne przy niektórych sytuacjach na planszy ale będzie niedługo

## **TODO:**
- [ ] dodać historię ruchów w `get_state`
- [ ] dodać możliwość pasowania w `send_state`
