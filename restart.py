@polygon.on(pattern="restart")
async def restart_interface(e):
    await e.edit("Polygon will be back soon!\nRun .ping to check if its back.")
    polygon.restart()