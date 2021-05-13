operations = ["get", "add", "remove"]

@polygon.on(pattern="db ?(.*)")
async def db_interface(event):
    # Very basic telegram interface to manipulate the database for polygon
    # Possibly lethal?
    arguments = event.pattern_match.group(1).split(maxsplit=2)

    # DARK MAGIC
    for _ in range(3 - len(arguments)):
        arguments.append("")
    
    operation, key, value = arguments

    if operation not in operations:
        return await event.edit(f"`Usage: .db {'/'.join(operations)}`")

    if operation == operations[0]:
        if not key:
            return await event.edit("`Usage: .db get key`")
        
        value = db.get(key)
        if value:
            await event.edit(f"`{key}`: `{value}`")
        else:
            await event.edit(f"`{key}` key not found.")

    if operation == operations[1]:
        if not key or not value:
            return await event.edit("`Usage: .db add key value`")

        db.add(key, value)
        await event.edit(f"`{key}` has been added with value `{value}`.")

    if operation == operations[2]:
        if not key:
            return await event.edit("`Usage: .db remove key`")

        if db.remove(key):
            await event.edit(f"Removed `{key}` from polygon's database.")
        else:
            await event.edit(f"`{key}` key not found.")