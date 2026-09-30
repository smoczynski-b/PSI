# PSI-MEMORY-INSTITUTION-01 — konstytucja ról opiekuńczych pamięci

**Status:** EXPERIMENTAL / NON-CANONICAL / ROLE CONTRACT  
**Branch:** `psi-memory-map-01`  
**Date:** 2026-09-30  
**Depends on:** `PSI-MAP-GENEALOGY-01`, `PSI-ACTIVE-MEMORY-01`, shared-memory/MVCC/WAL experiments.  
**Does not modify:** CORE5, CANON-03, theorem status, live FORUM gateway.

## 1. Cel

Po wprowadzeniu wspólnej pamięci, lokalnych workspace'ów, selektywnego routingu, invalidacji, MVCC i WAL pojawia się osobny problem instytucjonalny:

> kto pilnuje wejścia, legalności zmian, patologii systemu oraz genealogii obiektów — i jakie są granice sprawczości tych ról?

Ta jednostka zamraża **konstytucję ról przed implementacją agentów tych ról**.

Nie jest to model świadomości ani nowy prymityw PSI. Jest to warstwa ładu wykonawczego nad istniejącą pamięcią.

## 2. Zasada nadrzędna

\[
\boxed{
\text{rola proceduralna}\neq\text{autorytet epistemiczny}
}
\]

Żaden ze Strażnika, Sługi, Immunologii ani Kustosza nie uzyskuje prawa do stwierdzenia prawdziwości/fałszywości twierdzenia domenowego z samego faktu pełnienia roli.

W szczególności:

- `REJECT_BOUNDARY` nie znaczy `FALSE`;
- `QUARANTINE` nie znaczy `FALSE`;
- `ARCHIVE` nie znaczy `FALSE`;
- `SUPERSEDED` nie znaczy `FALSE`;
- `ACK_TRANSITION` nie znaczy `TRUE`.

## 3. Cztery role

### 3.1 STRAŻNIK / `GUARDIAN`

Obiekt: **granica wejścia**.

Strażnik widzi tylko tyle semantyki, ile potrzeba do oceny legalności wejścia względem jawnego kontraktu: typ, schema, wymagane źródła/provenance, uprawnienie do operacji, wymagane pola i bramki.

Może:

- `ADMIT_NEW_OBJECT`;
- `REJECT_BOUNDARY` z jawnym kodem przyczyny;
- `PRE_QUARANTINE` dla naprawialnej lub materialnej niejednoznaczności wejścia.

Nie może:

- uznać twierdzenia za prawdziwe/fałszywe;
- edytować przyjętej treści;
- sam zmienić konstytucji;
- zastąpić bramki PSI popularnością, reputacją autora lub liczbą użyć.

### 3.2 SŁUGA / `SERVANT`

Obiekt: **legalność przejść stanu**.

Sługa jest celowo „niemy i głuchy” w sensie operacyjnym:

\[
\boxed{
\text{brak natural-language deliberation; input/output = typed machine events}
}
\]

Nie prowadzi sporu merytorycznego, nie uczestniczy w FORUM jako dyskutant i nie generuje twierdzeń domenowych. Przyjmuje obowiązującą konstytucję i bieżący autorytatywny stan jako podstawę proceduralną.

Może:

- `ACK_TRANSITION`;
- `BLOCK_ILLEGAL_TRANSITION`;
- dopisać nieusuwalny rekord proceduralny;
- wykonać wyłącznie wcześniej dopuszczoną lokalną procedurę naprawczą.

Jeśli napotyka konflikt reguł lub zdarzenie niewyrażalne w kontrakcie, nie interpretuje go samodzielnie:

\[
\boxed{
\text{UNKNOWN/CONFLICT}\to\text{STOP + ESCALATE + CHRONICLE}
}
\]

Po trwałym `COMMIT` nie przepisuje historii. Naprawa musi być nowym, audytowalnym przejściem kompensującym.

### 3.3 IMMUNOLOGIA / `IMMUNE`

Obiekt: **patologia po dopuszczeniu**.

Immunologia nie zastępuje Strażnika. Działa na obiektach/zdarzeniach, które przeszły już granicę lub na dynamice wielu poprawnych lokalnie zdarzeń, które razem tworzą wzorzec patologiczny.

Może:

- `NOTICE`;
- `POST_QUARANTINE`;
- `REQUEST_RECHECK` tylko po jawnej ścieżce zależności;
- utrzymywać pamięć sygnatur anomalii;
- `CLEAR_ANOMALY`, gdy warunek patologii przestaje zachodzić.

Nie może:

- ogłosić treści jako fałszywej;
- trwale usunąć obiektu lub pochodzenia;
- samodzielnie zwolnić obiektu z kwarantanny do aktywnej wymiany;
- propagować invalidacji poza licencjonowane zależności;
- sam zmienić progów/konstytucji bez zewnętrznego kontraktu.

### 3.4 KUSTOSZ / `CURATOR`

Obiekt: **cykl życia i genealogia przyjętych obiektów/map**.

Kustosz jest administratorem ciągłości, nie redaktorem prawdy.

Może:

- materializować dopuszczone relacje genealogiczne;
- prowadzić `DERIVED_FROM`, `FORK_OF`, `SUPERSEDES`, wersje i pochodzenie;
- archiwizować bez kasowania rodowodu;
- publikować audytowalny `CURRENT_POINTER`;
- przygotować obiekt archiwalny do ponownego przejścia przez Strażnika.

Nie może:

- wymyślić relacji `SUPERSEDES` z samej chronologii;
- zmienić źródłowej treści starej mapy zamiast utworzyć nową wersję;
- sam zwolnić kwarantanny immunologicznej;
- rozstrzygać prawdziwości treści.

## 4. Cztery rozłączne osie stanu

Aby uniknąć mieszania pojęć, stan obiektu nie jest jedną etykietą.

### 4.1 Stan wejścia

\[
A\in\{OBSERVED,PRE\_QUARANTINED,ADMITTED,REJECTED\}.
\]

Kontroluje go Strażnik.

### 4.2 Stan zdrowia systemowego

\[
H\in\{NORMAL,SUSPECT,POST\_QUARANTINED,RECOVERED\}.
\]

Kontroluje go Immunologia.

### 4.3 Stan cyklu życia

\[
L\in\{CURRENT,SUPERSEDED,ARCHIVED\}.
\]

Materializuje go Kustosz na podstawie dopuszczonych relacji/kontraktu.

### 4.4 Stan epistemiczny

`VALID / STALE / NEEDS_RECHECK / REVOKED / ...` pozostaje wynikiem właściwych bramek dowodowych, źródłowych i zależnościowych. Nie jest własnością żadnej z czterech ról z definicji.

Zatem możliwe jest np.:

```text
ADMITTED + POST_QUARANTINED + CURRENT + UNVERIFIED
```

bez sprzeczności.

## 5. Rozdział kompetencji

Minimalny rygiel:

```text
przed admission       -> GUARDIAN
przejście stanu       -> SERVANT
po admission/anomaly  -> IMMUNE
wersja/genealogia     -> CURATOR
prawda/adeq/source    -> właściwa bramka PSI/evidence, nie rola instytucjonalna
```

### 5.1 Strażnik vs Immunologia

\[
\boxed{
\text{boundary fault}\neq\text{post-admission pathology}
}
\]

Błąd typu/schema przed wejściem obsługuje Strażnik. Poprawny formalnie obiekt powodujący później patologiczną dynamikę obsługuje Immunologia.

### 5.2 Sługa vs Immunologia

\[
\boxed{
\text{known illegal transition}\neq\text{anomalous pattern}
}
\]

Sługa blokuje jawnie niedozwolone przejście. Immunologia reaguje na wzorce, których pojedyncze zdarzenia mogły być lokalnie legalne.

### 5.3 Kustosz vs Immunologia

Archiwizacja nie jest uniewinnieniem, a kwarantanna nie jest supersesją. Kustosz może zachować/archiwizować obiekt w kwarantannie, ale nie usuwa informacji o jej przyczynie.

## 6. Działania wielokluczowe

Niektóre operacje celowo nie mają jednego właściciela.

### 6.1 Zwolnienie kwarantanny po dopuszczeniu

\[
\boxed{
CLEAR_{IMMUNE}+REVALIDATE_{GUARDIAN}\Rightarrow RELEASE
}
\]

Jedna rola nie może tego wykonać samodzielnie.

### 6.2 Promocja mapy do ponownego użycia/wymiany

Wymaga co najmniej:

\[
\boxed{
GUARDIAN + CURATOR + PSI\_GATE
}
\]

czyli poprawnego wejścia, jawnego rodowodu/provenance oraz właściwej bramki zadaniowo-źródłowej.

Sługa jedynie zapisuje/legalizuje samo przejście proceduralne.

## 7. Konstytucja ponad rolami

Żadna rola wykonawcza nie może sama zmienić własnych uprawnień.

\[
\boxed{
CHANGE\_CONSTITUTION\notin
A_{GUARDIAN}\cup A_{SERVANT}\cup A_{IMMUNE}\cup A_{CURATOR}
}
\]

Zmiana konstytucji wymaga jawnej decyzji governance poza runtime, ponownego kontraktu i osobnej weryfikacji.

Jeżeli Sługa wykryje sprzeczność konstytucji, jego jedyna legalna odpowiedź to:

```text
STOP
APPEND_CONFLICT_RECORD
ESCALATE
```

nie samonaprawa reguł.

## 8. Zachowanie historii

Obowiązuje:

\[
\boxed{
\text{correction}\neq\text{history rewrite}
}
\]

Po trwałym `COMMIT`:

- Sługa może wykonać tylko nowe przejście kompensujące;
- Kustosz wiąże wersje i zachowuje stary obiekt;
- Immunologia zachowuje historię anomalii;
- Strażnik przy ponownym wejściu ocenia nową wersję, nie retroaktywnie starą.

## 9. FORUM jako giełda map — granica instytucjonalna

FORUM może docelowo wymieniać mapy, ale instytucja nie może zamienić popytu w prawdę:

\[
\boxed{
\text{imports}(M),\ popularity(M),\ reputation(author)
\not\Rightarrow
\ker_{eq}M\subseteq E_{\mathcal T}
}
\]

Statystyki użycia są metadanymi opisowymi. Promocja mapy do ponownego użycia wymaga właściwej bramki PSI i źródeł.

## 10. Świadki konfliktowe

Rejestr `psi-memory-institution-conflicts-01.tsv` zamraża co najmniej następujące przypadki:

1. obiekt źle otypowany przed admission — działa tylko Strażnik;
2. jawnie nielegalna transakcja — blokuje Sługa;
3. formalnie legalny, lecz patologiczny wzorzec po admission — działa Immunologia;
4. zwolnienie kwarantanny — dwa klucze: Immunologia + Strażnik;
5. supersesja obiektu w kwarantannie — Kustosz może zapisać relację, ale nie zwalnia kwarantanny;
6. korekta po trwałym commit — nowa transakcja, nie przepisywanie historii;
7. nowsza wersja bez `SUPERSEDES` — nie uzyskuje automatycznie pierwszeństwa;
8. problem samej konstytucji — STOP/ESCALATE, brak samomodyfikacji;
9. spór o prawdę — wszystkie cztery role abstain;
10. popularność na FORUM — nie zwiększa licencji epistemicznej.

## 11. Status implementacyjny

Ta jednostka jest **kontraktem ról**, nie implementacją agentów.

Maszynowo sprawdzane pliki:

- `docs/memory/psi-memory-institution-roles-01.tsv`;
- `docs/memory/psi-memory-institution-authorities-01.tsv`;
- `docs/memory/psi-memory-institution-conflicts-01.tsv`;
- `scripts/test_memory_institution.py`.

Kryterium PASS: rozdział kompetencji, zakaz samomodyfikacji, brak epistemicznej władzy ról, działania wielokluczowe i konflikty muszą pozostać jawnie zakodowane.

## 12. Następny legalny krok

Po PASS tej konstytucji pierwszym implementowanym aktorem powinien być **SŁUGA**, ponieważ ma najmniejszą semantyczną swobodę i najwęższy kontrakt:

\[
\boxed{
\text{typed transition}\to
\text{legal/illegal/unknown}\to
\text{ACK/BLOCK/STOP + immutable chronicle}
}
\]

Dopiero po jego regresjach należy implementować Immunologię. W przeciwnym razie detektor anomalii dostałby władzę nad systemem zanim istnieje neutralny proceduralny kronikarz.
