from pathlib import Path

@polygon.on(pattern="logs")
async def logs_interface(e):
    log = Path("polygon.log")
    await e.edit("`Looking for logs..`")
    if log.exists():
        # We need to reverse the logs in order to show the lastest first
        reversed_logs = "".join(reversed(open(log, "r").readlines()))
        await e.respond(file=utility.buffer(reversed_logs, log.name))
        await e.delete()
    else:
        await e.edit("`Enable to find logfile [polygon.log].`")