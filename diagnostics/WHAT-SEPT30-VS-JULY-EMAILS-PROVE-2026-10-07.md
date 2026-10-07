# What the Nazeli emails prove — and what they do not

**Prepared:** 7 October 2026  
**This Cloud Agent:** `bc-3c3a1616-bd53-407e-8562-11da050498f8`  
**Exhibits:** PR #6 `docs/legal/exhibits/`  
**Not a legal opinion.** Counsel decides liability. This is a technical read of the documents.

---

## Direct answer

The 27–28 July emails plus the 30 September letter are **strong proof that 10Web’s access story is incomplete**. They are **not**, by themselves, a signed confession that 10Web “destroyed the website” as a legal conclusion.

They are still **core exhibits**. Save them. Use them. Do not over-claim them.

---

## What these exhibits *do* prove (document-to-document)

1. **10Web demanded WordPress admin access.**  
   Nazeli, 27–28 July 2026: create a temporary WP admin for `support@10web.io`; they will **access the existing WordPress dashboard** and migrate **from our end**.

2. **That demand came after their automation already failed**, and after Daniel reported **AI-bot fake sites** (26 July: “your ai bot made 2 fake websites pages, i deleted them”; UI said if reconnect fails, contact support; 15+ hours). 27 July email already names a 10Web-hosted site `active-bluegill.10web.cloud`.

3. **The 30 September letter rewrites that sequence.**  
   It says: after automated migration was unsuccessful, **you provided** admin access and **expressly authorized** Migration Assistant. It does **not** quote 10Web’s own “to proceed, please create a temporary administrator… we will proceed from our end.”

4. **10Web admits the migration was not successfully completed** and caused delay. They refuse damages, compensation, and a three-month refund. They offer a one-month subscription extension and say it is not an admission.

5. **DNS unchanged is not a defense to staging-file damage.**  
   The letter uses “source remained live / DNS not changed.” Staging can still be written (Manager plugin, `10web_tmp`, Migration Assistant, AI Builder) with DNS left alone. That was the safety rule *we* set; it does not mean Hostinger `tcstaging` was untouched.

---

## What they do *not* prove by themselves

| Claim | Why it is not closed by these four images |
| --- | --- |
| 10Web **restored over** source or **deleted** Hostinger backups | They deny it. The letter is not a confession. Need Hostinger restore-history export, Updraft missing `db.gz`, `10web_tmp` timing, WP revision timestamps. |
| **Every** visual defect on staging today is 10Web’s write | Recovery notes split three layers: (A) 10Web/Manager/AI/WP-access mash, (B) Hostinger Jul 24 uploads restore that **crushed Computers worse**, (C) Cursor Aug 12/19 light rebuilds that stripped catalogs further. If (B) and (C) are billed as 10Web, the file contradicts itself. |
| Unique SKU count “4000+ destroyed” | Owner testimony. This agent did not census 4000 SKUs. |
| Medical / housing / lost-revenue dollars | Not in these emails. |
| “Culpability” / legal liability | That is counsel + fact-finder. These exhibits prove **demand for access**, **fake Builder sites**, **failed migrate**, and a **later denial that omits the demand**. That is a strong **narrative and impeachment** package, not a verdict. |

---

## How to use it (accurate, not weak)

**Say:** 10Web’s migrator failed; they required WP admin to pull from their end; AI Builder fake sites already existed; after that period staging was not the pre-migration site; on 30 September they denied fault and recast the access they had demanded as Daniel’s idea.

**Do not say:** this PNG alone proves they deleted the backups and are legally guilty of destroying the website.

Pair for counsel:

| Exhibit | Job |
| --- | --- |
| p17 / p18 July emails | They **required** access |
| 26 Jul Daniel message on that thread | Fake sites + disconnect + contact support |
| 30 Sep denial | They **deny** and **reframe** access |
| BDM testimony PR #6 | Narrative glue |
| 8 Aug recovery memos on this branch | What was actually broken (classes, 404s, `10web_tmp`, CSS survived) |
| Hostinger restore table | Separate 24 Jul crush from 10Web writes |
