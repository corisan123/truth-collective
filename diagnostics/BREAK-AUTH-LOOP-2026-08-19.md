# BREAK AUTH LOOP (2026-08-19)

## What was wrong

The GPT worker on branch `cursor/computers-and-isi-b513` kept returning **401** on every REST probe.  
This lead environment has the same secret names and gets **HTTP 200** with `TC_WP_USER=dreid1253@yahoo.com`.

So the password is valid. The stuck agent is not receiving the same secret injection (wrong/missing Environment on that Cloud Agent run, or started before secrets existed).

## What we did (loop broken)

Lead applied **Office Workspace children** on staging now (6 pages). Do not wait on the stuck agent.

## Daniel: stop the stuck agent

1. Stop / archive the Cloud Agent that only reports 401.
2. New agents must use Environment **`truth-collective`** (or whichever Environment actually holds `TC_WP_USER` + `TC_WP_APP_PASSWORD`).
3. After launch, first message must print auth status. If 401, stop. Do not loop.
4. Regenerating the App Password is optional; linking the Environment is the usual fix.

## Next Block A

**Books children** — lead continues unless a new worker proves REST 200 first.
