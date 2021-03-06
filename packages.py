@polygon.on(pattern="addpkg ?(.*)")
async def pkg_interface_add(event):
    # Very basic telegram interface to add packages
    url = event.pattern_match.group(1)

    await event.edit("`Installing package..`")
    package_supported = polygon.add_package(url)

    if package_supported is True:
        await event.edit("`Installed package successfully.`")
    else:
        await event.edit(f"The following error occured while installing the package:\n{package_supported}")
    
@polygon.on(pattern="rmpkg ?(.*)")
async def pkg_interface_remove(event):
    # Very basic telegram interface to remove packages
    name = event.pattern_match.group(1)
    if polygon.remove_package(name):
        await event.edit(f"Removed package `{name}` successfully.")
    else:
        await event.edit(f"Package `{name}` not found.")

@polygon.on(pattern="pkgs")
async def pkg_interface_list(event):
    # Very basic telegram interface to list packages
    if not polygon.packages:
        return await event.edit("`No packages have been loaded yet.`")
    packages = "**All loaded packages:**\n\n" + "\n".join([f"~` {name}`" for name in polygon.packages])
    await event.edit(packages)