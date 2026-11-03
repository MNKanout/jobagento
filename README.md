<div align="center">

# JobAgento

**A team of AI agents that finds jobs, tailors your CV and cover letter to each one, fact-checks them, and fills in the application form. You press send.**

![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-D97757?logo=anthropic&logoColor=white)

### [▶ jobagento.com](https://jobagento.com)

<a href="https://jobagento.com"><img src="https://jobagento.com/og.jpg" width="100%" alt="JobAgento: a team of AI agents that finds jobs for you, next to a 3D office where the agents work."></a>

</div>

## What it is

JobAgento is a Claude Code plugin. It runs in your own Claude Code, on your own Claude plan, and keeps your data on the hosted JobAgento server behind your login. Watch your agents work in JobAgento HQ, a live 3D office, at [jobagento.com](https://jobagento.com).

| | |
|---|---|
| 🔎 **Find** | Searches job boards in the countries you pick for the job titles you want. |
| 🎯 **Match** | Scores each posting against your CV, ranks its most important terms, and skips poor fits. |
| 📝 **Tailor** | Rewrites your CV and writes a cover letter for that one job, using only facts from your real CV. |
| 🛡️ **Check** | A proofreading agent checks the CV, the letter and the printed pages, and sends anything wrong back until everything passes. |
| ✍️ **Fill in** | An agent fills the application form in a visible browser and stops before the send button. **You read it and press send.** |

## Get started

You need Claude Code, Python 3.10+, Google Chrome, Node.js and poppler. The plugin checks for them when a session starts.

1. Add the plugin in Claude Code:
   ```
   /plugin marketplace add MNKanout/jobagento
   /plugin install jobagento@jobagento
   ```
2. Sign in: run `/mcp`, choose the jobagento plugin's **jobs** server, and enter your email and the code you get.
3. Run `/jobagento:setup` once: your CV, contact details, job titles and countries.
4. Start a run with `/jobagento:find-and-apply`.

Every command is in [the plugin guide](plugin/README.md).

**Coming from Job Hunt AI?** It's the same plugin under its new name. Run `/plugin uninstall job-hunt-ai`, then follow the steps above.

## License

[PolyForm Noncommercial 1.0.0](LICENSE): free to use, study and change for non-commercial purposes, such as your own job search. Commercial use, including reselling it or offering it as a service, is not permitted. This makes the project source-available, not open source.

Each user is responsible for using job boards and employer sites within their own terms.

<div align="center">

Built by [Nour Kanout](https://github.com/MNKanout)

</div>
