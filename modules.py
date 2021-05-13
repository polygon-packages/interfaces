@polygon.on(pattern="load")
async def module_interface_load(event):
    module = await event.get_reply_message()
    if not module:
        return await event.edit("`Reply to a module to load it.`")
    await event.edit("`Loading module..`")
    path = polygon.path / "modules" / module.file.name
    name = path.stem

    if path.exists():
        await event.edit("`Module already exists, overwriting..`")
        polygon.unload_module(name)
        path.unlink()

    await polygon.download_media(module, path.parent)
    module_supported = polygon.load_module(name) 
    if module_supported is not True:
        return await event.edit(f"The following error occurred while loading the module:\n`{module_supported}`")
    await event.edit(f"`Loaded module {name} successfully!`")

@polygon.on(pattern="unload ?(.*)")
async def module_interface_unload(event):
    name = event.pattern_match.group(1)
    module = polygon.modules.get(name)
    if not name:
        return await event.edit("`Usage: .unload module_name`")
    if not module or not module.exists():
        return await event.edit(f"404: `{name}` module not found.")
    polygon.unload_module(name)
    await event.edit(f"Unloaded module `{name}` successfully!")