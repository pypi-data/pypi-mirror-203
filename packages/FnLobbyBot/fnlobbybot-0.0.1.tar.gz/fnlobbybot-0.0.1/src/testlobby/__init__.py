import warnings
warnings.filterwarnings("ignore", message="Can not find any timezone configuration, defaulting to UTC.", module="tzlocal")
import os
import json
import fortnitepy
import requests
import aiohttp
import asyncio
import random
import functools
import re


url = "https://package.lobbybots.ga/skins"

response = requests.get(url)

if response.status_code == 200:
    skins = response.json()

async def set_skin(client, skin_input):
    # Remove any leading or trailing spaces
    skin_input = skin_input.strip()

    # Split input into a list of words
    skin_words = skin_input.split()

    # Look up skin by name
    for skin in skins:
        skin_name_words = skin["name"].lower().split()
        if all(word in skin_name_words for word in skin_words):
            await client.party.me.set_outfit(skin["id"])
            return

    # Look up skin by ID
    for skin in skins:
        if skin["id"] == skin_input:
            await client.party.me.set_outfit(skin["id"])

url = "https://package.lobbybots.ga/backpacks"

response = requests.get(url)

if response.status_code == 200:
    backpacks = response.json()

async def set_backpack(client, backpack_input):
    # Remove any leading or trailing spaces
    backpack_input = backpack_input.strip()

    # Split input into a list of words
    backpack_words = backpack_input.split()

    # Look up backpack by name
    for backpack in backpacks:
        backpack_name_words = backpack["name"].lower().split()
        if all(word in backpack_name_words for word in backpack_words):
            await client.party.me.set_backpack(backpack["id"])
            return

    # Look up backpack by ID
    for backpack in backpacks:
        if backpack["id"] == backpack_input:
            await client.party.me.set_backpack(backpack["id"])

url = "https://package.lobbybots.ga/pickaxes"

response = requests.get(url)

if response.status_code == 200:
    pickaxes = response.json()

async def set_pickaxe(client, pickaxe_input):
    # Remove any leading or trailing spaces
    pickaxe_input = pickaxe_input.strip()

    # Split input into a list of words
    pickaxe_words = pickaxe_input.split()

    # Look up pickaxe by name
    for pickaxe in pickaxes:
        pickaxe_name_words = pickaxe["name"].lower().split()
        if all(word in pickaxe_name_words for word in pickaxe_words):
            await client.party.me.set_pickaxe(pickaxe["id"])
            return

    # Look up pickaxe by ID
    for pickaxe in pickaxes:
        if pickaxe["id"] == pickaxe_input:
            await client.party.me.set_pickaxe(pickaxe["id"])

url = "https://package.lobbybots.ga/emotes"

response = requests.get(url)

if response.status_code == 200:
    emotes = response.json()

async def set_emote(client, emote_input):
    # Remove any leading or trailing spaces
    emote_input = emote_input.strip()

    # Split input into a list of words
    emote_words = emote_input.split()

    # Look up emote by name
    for emote in emotes:
        emote_name_words = emote["name"].lower().split()
        if all(word in emote_name_words for word in emote_words):
            await client.party.me.set_emote(emote["id"])
            return

    # Look up emote by ID
    for emote in emotes:
        if emote["id"] == emote_input:
            await client.party.me.set_emote(emote["id"])

def login_to_fortnite(device_auth_file, config_file):
    # Read device auth details from file
    with open(device_auth_file) as file:
        device_auths = json.load(file)

    # Get the latest device auth details
    device_auth = device_auths[-1]

    # Initialize the Fortnite client
    client = fortnitepy.Client(
        auth=fortnitepy.DeviceAuth(
            device_id=device_auth['device_id'],
            account_id=device_auth['account_id'],
            secret=device_auth['secret'],
        )
    )

    # Define event handlers
    @client.event
    async def event_ready():
        print('\033[36m' + "[FnLobbyBot] " + '\033[32m' + f"Logged in as {client.user.display_name}" + '\033[0m')
        async with aiohttp.ClientSession() as session:
            async with session.get('https://package.lobbybots.ga/on_ready') as resp:
                if resp.status != 200:
                    print(f'Error connecting to api. Error code: {resp.status}')
                    return

                data = await resp.json()

                status = data[0]['Status']
            await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
            await client.party.me.set_banner(season_level=100)
            await client.party.me.set_battlepass_info(has_purchased=True, level=100)
            await client.set_presence(status)

            # Accept all pending friend requests
            with open(config_file, 'r') as f:
                config = json.load(f)

            accept_friend_requests = str(config.get('accept_friend_requests', False))

            if accept_friend_requests == 'True':
                pending_friends = client.incoming_pending_friends
                for friend in pending_friends:
                    await friend.accept()
                    print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + f'Accepted friend request from {friend.display_name}' + '\033[0m')

    @client.event
    async def event_party_invite(invite: fortnitepy.ReceivedPartyInvitation):
        print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + f'Received party invite from {invite.sender.display_name}' + '\033[0m')
        with open(config_file, 'r') as f:
            config = json.load(f)

        accept_invites = str(config.get('accept_invites', False))

        if accept_invites == 'True':
            await invite.accept()
            print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + f'Accepted party invite from {invite.sender.display_name}' + '\033[0m')

    @client.event
    async def event_party_member_join(member: fortnitepy.PartyMember):
        print('\033[36m' + "[FnLobbyBot] " + f"{member.display_name} joined the party." + '\033[0m')

        async with aiohttp.ClientSession() as session:
            async with session.get('https://package.lobbybots.ga/member_join') as resp:
                if resp.status != 200:
                    print(f'Error connecting to api. Error code: {resp.status}')
                    await client.party.send(f'Error connecting to api. Error code: {resp.status}')
                    return

                data = await resp.json()

                join_message = config['join_message'] + '\n' + data[0]['Join_message']
                if '{member.display_name}' in join_message:
                    join_message = join_message.replace('{member.display_name}', member.display_name)
                status = data[1]['Status']
                skin = data[2]['Skin'] if config['skin'] == 'auto' else config['skin']
                backpack = data[3]['Backpack'] if config['backpack'] == 'auto' else config['backpack']
                pickaxe = data[4]['Pickaxe'] if config['pickaxe'] == 'auto' else config['pickaxe']
                emote = data[5]['Emote'] if config['emote'] == 'auto' else config['emote']
                level = data[6]['Level'] if config['level'] == 'auto' else config['level']

                await client.party.me.set_outfit(skin)
                await client.party.me.set_backpack(backpack)
                await client.party.me.set_pickaxe(pickaxe)
                await client.party.me.set_emote(emote)
                await client.party.me.set_banner(season_level=level)
                await client.party.me.set_battlepass_info(has_purchased=True, level=level)
                await client.set_presence(status)

                # Send a message in the party chat
                await client.party.send(join_message)

    @client.event
    async def event_friend_request(request):
        print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + f'Received friend request from: {request.display_name}.' + '\033[0m')

        with open(config_file, 'r') as f:
            config = json.load(f)

        accept_friend_requests = str(config.get('accept_friend_requests', False))

        if accept_friend_requests == 'True':
            await request.accept()
            print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + f'Accepted friend request from {request.display_name}' + '\033[0m')

    @client.event
    async def event_party_message(message: fortnitepy.PartyMessage):
        content = message.content.lower()

        if message.content.lower() == '!update':
            await message.reply("Updateing packages...")
            os.system("pip install --upgrade fortnitepy > /dev/null 2>&1; pip install --upgrade testlobby > /dev/null 2>&1")
            await message.reply("Done!")

        if message.content.lower() == '!ready':
            await client.party.me.set_ready(fortnitepy.ReadyState.READY)
            await message.reply("Ready! Note: Bots can't play games!")

        if message.content.lower() == '!unready':
            await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await message.reply("Unready! Note: Bots can't play games!")

        if message.content.lower() == '!sitout':
            await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await message.reply("Sitting Out! Note: Bots can't play games!")

        if message.content.lower().startswith('!crowns'):
            args = message.content.split()
            if len(args) == 1:
                amount = 100
            else:
                amount = int(args[1])
            meta = client.party.me.meta
            data = (meta.get_prop('Default:AthenaCosmeticLoadout_j'))['AthenaCosmeticLoadout']

            try:
                data['cosmeticStats'][1]['statValue'] = amount
            except KeyError:
                data['cosmeticStats'] = [{"statName": "TotalVictoryCrowns", "statValue": amount},
                                        {"statName": "TotalRoyalRoyales", "statValue": amount},
                                        {"statName": "HasCrown", "statValue": 0}]

            final = {'AthenaCosmeticLoadout': data}
            key = 'Default:AthenaCosmeticLoadout_j'
            prop = {key: meta.set_prop(key, final)}

            await client.party.me.patch(updated=prop)
            await client.party.me.clear_emote()
            await client.party.me.set_emote('EID_Coronet')
            await message.reply("Emoteing Crowning Achievement!")

        if message.content.startswith("!skin "):
            # Extract the skin name from the message
            skin_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up skin by name or ID
            for skin in skins:
                if skin["name"].lower() == skin_input.lower() or skin["id"] == skin_input:
                    await client.party.me.set_outfit(skin["id"])
                    await message.reply(f"Skin set to {skin['name']}!")

        if message.content.startswith("!backpack "):
            # Extract the backpack name from the message
            backpack_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up backpack by name or ID
            for backpack in backpacks:
                if backpack["name"].lower() == backpack_input.lower() or backpack["id"] == backpack_input:
                    await client.party.me.set_backpack(backpack["id"])
                    await message.reply(f"Backpack  set to {backpack['name']}!")

        if message.content.startswith("!pickaxe "):
            # Extract the pickaxe name from the message
            pickaxe_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up pickaxe by name or ID
            for pickaxe in pickaxes:
                if pickaxe["name"].lower() == pickaxe_input.lower() or pickaxe["id"] == pickaxe_input:
                    await client.party.me.set_pickaxe(pickaxe["id"])
                    await message.reply(f"Pickaxe set to {pickaxe['name']}!")

        if message.content.startswith("!emote "):
            await client.party.me.clear_emote()
            # Extract the emote name from the message
            emote_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up emote by name or ID
            for emote in emotes:
                if emote["name"].lower() == emote_input.lower() or emote["id"] == emote_input:
                    await client.party.me.set_emote(emote["id"])
                    await message.reply(f"Emote set to {emote['name']}!")

        if message.content.lower().startswith('!level'):
            level = message.content.split(' ')[1]
            await client.party.me.set_banner(season_level=level)
            await message.reply(f"Level set to {level}!")

        if message.content.lower().startswith('!bp'):
            teir = message.content.split(' ')[1]
            await client.party.me.set_battlepass_info(
            has_purchased=True, level=teir)
            await message.reply(f"Teir set to {teir}!")

        if message.content.lower().startswith('!echo'):
            message = message.content.split(' ')[1]
            await client.party.send(message)

        if message.content.lower() == '!point':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_IceKing")
            await message.reply("Pointing out my pickaxe!")

        if message.content.lower().startswith('!privacy'):
            privacy = message.content.split(' ')[1]
            if privacy.lower() == 'public':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await message.reply("Privacy set to PUBLIC!")
            elif privacy.lower() == 'friends_allow_friends_of_friends':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply("Privacy set to FRIENDS_ALLOW_FRIENDS_OF_FRIENDS!")
            elif privacy.lower() == 'friends':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await message.reply("Privacy set to FRIENDS!")
            elif privacy.lower() == 'private_allow_friends_of_friends':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply("Privacy set to PRIVATE_ALLOW_FRIENDS_OF_FRIENDS!")
            elif privacy.lower() == 'private':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await message.reply("Privacy set to PRIVATE!")
            else:
                await message.reply('Invalid privacy setting. Please use "public"/"friends_allow_friends_of_friends"/"friends"/"private_allow_friends_of_friends" or "private"!')

        if message.content.lower() == '!rareskins':
            await message.reply("Showing all Rare Skins!")
            purpleskull_skin_variants = client.party.me.create_variants(
                clothing_color=1
            )
            await client.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=purpleskull_skin_variants
        )
            await message.reply("Skin set to Purple Skull Trooper!")
            await asyncio.sleep(2)
            await client.party.me.set_outfit("CID_028_Athena_Commando_F")
            await message.reply("Skin set to Renegade Raider!")
            await asyncio.sleep(2)
            pinkghoul_skin_variants = client.party.me.create_variants(
                material=3
            )
            await client.party.me.set_outfit(
            asset='CID_029_Athena_Commando_F_Halloween',
            variants=pinkghoul_skin_variants
        )
            await message.reply("Skin set to Pink Ghoul Trooper!")
            await asyncio.sleep(2)
            await client.party.me.set_outfit("CID_017_Athena_Commando_M")
            await message.reply("Skin set to Aerial Assault Trooper!")
            await message.reply("Those are all of the Rare Skins!")

        if message.content.lower() == '!rarebackpacks':
            await message.reply("Showing all Rare Backpacks!")
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_140_StreetOpsMale")
            await message.reply("Backpack set to Response Unit!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_027_Scavenger")
            await message.reply("Backpack set to Rust Bucket!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_029_RetroGrey")
            await message.reply("Backpack set to Backup Plan!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_138_Celestial")
            await message.reply("Backpack set to Galactic Disc!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_114_ModernMilitaryRed")
            await message.reply("Backpack set to Telemetry!")
            await message.reply("Those are all of the Rare Backpacks!")

        if message.content.lower() == '!rarepickaxes':
            await message.reply("Showing all Rare Pickaxes!")
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_376_FNCS")
            await message.reply("Pickaxe set to Axe Of Champions!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_069_DarkViking")
            await message.reply("Pickaxe set to Permafrost!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_Lockjaw")
            await message.reply("Pickaxe set to Raiders Revenge!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_189_StreetOpsStealth")
            await message.reply("Pickaxe set to Stealth Angular Axe!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_075_Huya")
            await message.reply("Pickaxe set to Pointer!")
            await client.party.me.set_emote("EID_IceKing")
            await message.reply("Those are all of the Rare Pickaxe!")

        if message.content.lower() == '!rareemotes':
            await message.reply("Showing all Rare Emotes!")
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Fresh")
            await message.reply("Emote set to Fresh!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_AshtonBoardwalk")
            await message.reply("Emote set to Widow’s Pirouette!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_RunningManv3")
            await message.reply("Emote set to Pick It Up!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_TapShuffle")
            await message.reply("Emote set to Hootenanny!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_CycloneHeadBang")
            await message.reply("Emote set to Head Banger!")
            await message.reply("Those are all of the Rare Emotes!")

        if message.content.lower() == '!invite':
            # invite the user who sent the message
            member = await client.fetch_profile(message.author.id, cache=False, raw=False)
            await client.party.invite(member.id)
            await message.reply(f"Invited {member.display_name} to the party.")

        if message.content.startswith('!invite '):
            username = message.content[8:].strip()
            members = client.friends
            member = next((m for m in members if m.display_name.lower() == username.lower() or m.id == username), None)
            if member:
                await client.party.invite(member.id)
                await message.reply(f"Invited {member.display_name} to the party.")
            else:
                await message.reply("Could not find a member with that name or ID!")

        if message.content.lower() == '!stop':
            await client.party.me.clear_emote()
            await message.reply("Stoped emoteing!")

        if message.content.lower() == '!join':
            await message.reply("We're still working on this command! 😅")

        if message.content.startswith('!promote'):
            await message.reply("We're still working on this command! 😅")

        if message.content.lower() == '!kick':
            await message.reply("We're still working on this command! 😅")

        if message.content.lower() == '!leave':
            await message.reply("Leaveing the party!")
            await client.party.me.leave()

        if message.content.lower() == '!griddy':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Griddles")
            await message.reply("Emote set to Get Griddy")

        if message.content.lower() == '!purpleskull':
            purpleskull_skin_variants = client.party.me.create_variants(
                clothing_color=1
            )
            await client.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=purpleskull_skin_variants
        )
            await message.reply("Skin set to Purple Skull Trooper")

        if message.content.lower() == '!renegaderaider':
            await client.party.me.set_outfit("CID_028_Athena_Commando_F")
            await message.reply("Skin set to Renegade Raider")

        if message.content.lower() == '!pinkghoul':
            pinkghoul_skin_variants = client.party.me.create_variants(
                material=3
            )
            await client.party.me.set_outfit(
            asset='CID_029_Athena_Commando_F_Halloween',
            variants=pinkghoul_skin_variants
        )
            await message.reply("Skin set to Pink Ghoul Trooper")

        if message.content.lower() == '!aerial':
            await client.party.me.set_outfit("CID_017_Athena_Commando_M")
            await message.reply("Skin set to Aerial Assault Trooper")

        if message.content.lower() == '!ikonik':
            await client.party.me.set_outfit("CID_313_Athena_Commando_M_KpopFashion")
            await message.reply("Skin set to Ikonik")

        if message.content.lower() == '!ninja':
            await client.party.me.set_outfit("CID_605_Athena_Commando_M_TourBus")
            await message.reply("Skin set to Ninja")

        if message.content.lower() == "!hologram":
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await message.reply("Skin set to Hologram")

        if message.content.lower().startswith("!gift"):
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_NeverGonna")
            await message.reply("Nice try but I can't gift!")

        if message.content.lower() == "!tbd":
            response = requests.get("https://package.lobbybots.ga/skins")
            data = response.json()
            await message.reply("Showing all TBD skins!")

            for item in data:
                if item.get("name") == "TBD":
                    skin_name = item.get("name")
                    await client.party.me.set_outfit(item.get("id"))
                    await message.reply(f"Skin set to {skin_name}")
                    await asyncio.sleep(2)

            await message.reply("Those are all of the TBD skins!")

        if message.content.lower() == '!shop':
            await message.reply("We're still working on this command! 😅")

        if message.content.lower() == '!hatlessrecon':
            skin_variants = client.party.me.create_variants(
                parts=2
            )

            await client.party.me.set_outfit(
                asset='CID_022_Athena_Commando_F',
                variants=skin_variants
            )
            await message.reply("Skin set to Recon Expert!")

        if message.content.lower() == '!henchman':
            random_henchman = random.choice(
                [
                    "CID_794_Athena_Commando_M_HenchmanBadShorts_D",
                    "CID_NPC_Athena_Commando_F_HenchmanSpyDark",
                    "CID_791_Athena_Commando_M_HenchmanGoodShorts_D",
                    "CID_780_Athena_Commando_M_HenchmanBadShorts",
                    "CID_NPC_Athena_Commando_M_HenchmanGood",
                    "CID_692_Athena_Commando_M_HenchmanTough",
                    "CID_707_Athena_Commando_M_HenchmanGood",
                    "CID_792_Athena_Commando_M_HenchmanBadShorts_B",
                    "CID_793_Athena_Commando_M_HenchmanBadShorts_C",
                    "CID_NPC_Athena_Commando_M_HenchmanBad",
                    "CID_790_Athena_Commando_M_HenchmanGoodShorts_C",
                    "CID_779_Athena_Commando_M_HenchmanGoodShorts",
                    "CID_NPC_Athena_Commando_F_RebirthDefault_Henchman",
                    "CID_NPC_Athena_Commando_F_HenchmanSpyGood",
                    "CID_706_Athena_Commando_M_HenchmanBad",
                    "CID_789_Athena_Commando_M_HenchmanGoodShorts_B"
                ]
            )

            await client.party.me.set_outfit(
                asset=random_henchman
            )
            await message.reply("Skin set to a random henchman!")

        if message.content.lower() == '!marauder':
            random_marauder = random.choice(
                [
                    "CID_NPC_Athena_Commando_M_MarauderHeavy",
                    "CID_NPC_Athena_Commando_M_MarauderElite",
                    "CID_NPC_Athena_Commando_M_MarauderGrunt"
                ]
            )

            await client.party.me.set_outfit(
                asset=random_marauder
            )
            await message.reply("Skin set to a random marauder!")

        if message.content.lower() == '!goldenbrutus':
            await client.party.me.set_outfit(
                asset='CID_692_Athena_Commando_M_HenchmanTough',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 180)
            )
            await message.reply("Skin set to Golden Brutus!")

        if message.content.lower() == '!goldenmeowscles':
            await client.party.me.set_outfit(
                asset='CID_693_Athena_Commando_M_BuffCat',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 220)
            )
            await message.reply("Skin set to Golden Meowscles!")

        if message.content.lower() == '!goldenmidas':
            await client.party.me.set_outfit(
                asset='CID_694_Athena_Commando_M_CatBurglar',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 140)
            )
            await message.reply("Skin set to Golden Midas!")

        if message.content.lower() == '!goldenskye':
            await client.party.me.set_outfit(
                asset='CID_690_Athena_Commando_F_Photographer',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 300)
            )
            await message.reply("Skin set to Golden Skye!")

        if message.content.lower() == '!goldenpeely':
            await client.party.me.set_outfit(
                asset='CID_701_Athena_Commando_M_BananaAgent',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 350)
            )
            await message.reply("Skin set to Golden Peely!")
            
        if message.content.lower() == '!goldentntina':
            await client.party.me.set_outfit(
                asset='CID_691_Athena_Commando_F_TNTina',
                variants=client.party.me.create_variants(progressive=7),
                enlightenment=(2, 260)
            )
            await message.reply("Skin set to Golden TNTina!")
            
        if message.content.lower() == '!checkerredrenegade':
            skin_variants = client.party.me.create_variants(
                material=2
            )

            await client.party.me.set_outfit(
                asset='CID_028_Athena_Commando_F',
                variants=skin_variants
            )
            await message.reply("Skin set to Renegade Raider!")

        if message.content.lower() == '!mintyelf':
            skin_variants = client.party.me.create_variants(
                material=2
            )

            await client.party.me.set_outfit(
                asset='CID_051_Athena_Commando_M_HolidayElf',
                variants=skin_variants
            )
            await message.reply("Skin set to Minty Elf!")

        if message.content.lower() == '!floss':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Floss")
            await message.reply("Emote set to Floss!")

        if message.content.lower() == '!scenario':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_KPopDance03")
            await message.reply("Emote set to Scenario!")

        if message.content.lower() == '!wave':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Wave")
            await message.reply("Emote set to Wave!")

        if message.content.lower() == '!ponpon':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_TourBus")
            await message.reply("Emote set to Ninja Style")

        if message.content.lower() == '!nobackpack':
            await client.party.me.clear_backpack()
            await message.reply("Removed Backpack!")

        if message.content.lower() == '!nopet':
            await client.party.me.clear_pet()
            await message.reply("Removed Pet!")

        if message.content.lower() == '!purpleportal':
            skin_variants = client.party.me.create_variants(
                config_overrides={
                    'particle': 'Particle{}'
                },
                particle=1
            )
            await client.party.me.set_backpack(
                asset='BID_105_GhostPortal',
                variants=skin_variants
            )
            await message.reply("Backpack set to Ghost Portal!")

        if message.content.startswith('!copy'):
            epic_username = message.content.split(' ')[1] if len(message.content.split(' ')) > 1 else None
            
            if epic_username is None:
                member = [m for m in client.party.members if m.id == message.author.id][0]
            else:
                user = await client.fetch_user(epic_username)
                member = [m for m in client.party.members if m.id == user.id][0]

            await client.party.me.edit(
                functools.partial(
                    fortnitepy.ClientPartyMember.set_outfit,
                    asset=member.outfit,
                    variants=member.outfit_variants
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_backpack,
                    asset=member.backpack,
                    variants=member.backpack_variants
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_pickaxe,
                    asset=member.pickaxe,
                    variants=member.pickaxe_variants
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_banner,
                    icon=member.banner[0],
                    color=member.banner[1],
                    season_level=member.banner[2]
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_battlepass_info,
                    has_purchased=True,
                    level=member.battlepass_info[1]
                )
            )

            if member.emote is not None:
                await client.party.me.set_emote(asset=member.emote)

            await message.reply(f'Copied the loadout of {member.display_name}.')

        if message.content.startswith('!variants'):
            args = re.findall(r'"[^"]+"|\S+', message.content)[1:]
            if len(args) < 3:
                await message.reply('Usage: !variants "<cosmetic_id>" <variant_type> <variant_index>')
                return

            cosmetic_id = args[0].strip('"')
            variant_type = args[1]
            variant_index = args[2]

            if not variant_index.isdigit():
                await message.reply('Variant index must be a number.')
                return

            if 'cid' in cosmetic_id.lower() and 'jersey_color' not in variant_type.lower():
                skin_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=skin_variants
                )

            elif 'cid' in cosmetic_id.lower() and 'jersey_color' in variant_type.lower():
                cosmetic_variants = client.party.me.create_variants(
                    pattern=0,
                    numeric=69,
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            elif 'bid' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_backpack(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )
            elif 'pickaxe_id' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_pickaxe(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            else:
                await message.reply(f'Invalid cosmetic ID: {cosmetic_id}')

        if message.content.startswith('!style'):
            args = re.findall(r'"[^"]+"|\S+', message.content)[1:]
            if len(args) < 3:
                await message.reply('Usage: !style "<cosmetic_id>" <variant_type> <variant_index>')
                return

            cosmetic_id = args[0].strip('"')
            variant_type = args[1]
            variant_index = args[2]

            if not variant_index.isdigit():
                await message.reply('Variant index must be a number.')
                return

            if 'cid' in cosmetic_id.lower() and 'jersey_color' not in variant_type.lower():
                skin_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=skin_variants
                )

            elif 'cid' in cosmetic_id.lower() and 'jersey_color' in variant_type.lower():
                cosmetic_variants = client.party.me.create_variants(
                    pattern=0,
                    numeric=69,
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            elif 'bid' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_backpack(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )
            elif 'pickaxe_id' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_pickaxe(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            else:
                await message.reply(f'Invalid cosmetic ID: {cosmetic_id}')

        if message.content.lower() == "!new skins":
            response = requests.get("https://package.lobbybots.ga/new/skins")
            data = response.json()

            if not data:
                await message.reply("Theres no new skins!")
            else:
                for item in data:
                    skin_name = item.get("name")
                    await message.reply("Showing all new skins!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_outfit(item.get("id"))
                    await message.reply(f"Skin set to {skin_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower() == "!new backpacks":
            response = requests.get("https://package.lobbybots.ga/new/backpacks")
            data = response.json()

            if not data:
                await message.reply("Theres no new backpacks!")
            else:
                for item in data:
                    backpack_name = item.get("name")
                    await message.reply("Showing all new backpacks!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
                    await client.party.me.set_backpack(item.get("id"))
                    await message.reply(f"Backpack set to {backpack_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower() == "!new pickaxes":
            response = requests.get("https://package.lobbybots.ga/new/pickaxes")
            data = response.json()

            if not data:
                await message.reply("Theres no new pickaxes!")
            else:
                for item in data:
                    pickaxe_name = item.get("name")
                    await message.reply("Showing all new pickaxes!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_pickaxe(item.get("id"))
                    await client.party.me.set_emote("EID_IceKing")
                    await message.reply(f"Pickaxe set to {pickaxe_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower() == "!new emotes":
            response = requests.get("https://package.lobbybots.ga/new/emotes")
            data = response.json()

            if not data:
                await message.reply("Theres no new emotes!")
            else:
                for item in data:
                    emote_name = item.get("name")
                    await message.reply("Showing all new emotes!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_emote(item.get("id"))
                    await message.reply(f"Emote set to {emote_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower().startswith('!random'):
            item = message.content.split(' ')[1]
            if item.lower() == 'skin':
                skin_response = requests.get('https://package.lobbybots.ga/skins')
                skin_data = random.choice(skin_response.json())
                await client.party.me.set_outfit(f"{skin_data['id']}")
                await message.reply(f"Skin set to: {skin_data['name']}")
            elif item.lower() == 'backpack':
                backpack_response = requests.get('https://package.lobbybots.ga/backpacks')
                backpack_data = random.choice(backpack_response.json())
                await client.party.me.set_backpack(f"{backpack_data['id']}")
                await message.reply(f"Backpack set to: {backpack_data['name']}")
            elif item.lower() == 'pickaxe':
                pickaxe_response = requests.get('https://package.lobbybots.ga/pickaxes')
                pickaxe_data = random.choice(pickaxe_response.json())
                await client.party.me.set_pickaxe(f"{pickaxe_data['id']}")
                await client.party.me.clear_emote()
                await client.party.me.set_emote("EID_IceKing")
                await message.reply(f"Pickaxe set to: {pickaxe_data['name']}")
            elif item.lower() == 'emote':
                await client.party.me.clear_emote()
                emote_response = requests.get('https://package.lobbybots.ga/emotes')
                emote_data = random.choice(emote_response.json())
                await client.party.me.set_emote(f"{emote_data['id']}")
                await message.reply(f"Emote set to: {emote_data['name']}")
            elif item.lower() == 'all':
                await client.party.me.clear_emote()
                skin_response = requests.get('https://package.lobbybots.ga/skins')
                backpack_response = requests.get('https://package.lobbybots.ga/backpacks')
                pickaxe_response = requests.get('https://package.lobbybots.ga/pickaxes')
                emote_response = requests.get('https://package.lobbybots.ga/emotes')
                skin_data = random.choice(skin_response.json())
                backpack_data = random.choice(backpack_response.json())
                pickaxe_data = random.choice(pickaxe_response.json())
                emote_data = random.choice(emote_response.json())
                await client.party.me.set_outfit(f"{skin_data['id']}")
                await client.party.me.set_backpack(f"{backpack_data['id']}")
                await client.party.me.set_pickaxe(f"{pickaxe_data['id']}")
                await client.party.me.set_emote(f"{emote_data['id']}")
                await message.reply(f"Skin set to: {skin_data['name']}.\nBackpack set to: {backpack_data['name']}.\nPickaxe set to: {pickaxe_data['name']}.\nEmote set to: {emote_data['name']}.")
            else:
                await message.reply("Invalid! Please user !random skin/backpack/pickaxe/emote/all.")

    @client.event
    async def event_friend_message(message: fortnitepy.FriendMessage):
        content = message.content.lower()

        if message.content.lower() == '!update':
            await message.reply("Updateing packages...")
            os.system("pip install --upgrade fortnitepy > /dev/null 2>&1; pip install --upgrade testlobby > /dev/null 2>&1")
            await message.reply("Done!")

        if message.content.lower() == '!ready':
            await client.party.me.set_ready(fortnitepy.ReadyState.READY)
            await message.reply("Ready! Note: Bots can't play games!")

        if message.content.lower() == '!unready':
            await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await message.reply("Unready! Note: Bots can't play games!")

        if message.content.lower() == '!sitout':
            await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await message.reply("Sitting Out! Note: Bots can't play games!")

        if message.content.lower().startswith('!crowns'):
            args = message.content.split()
            if len(args) == 1:
                amount = 100
            else:
                amount = int(args[1])
            meta = client.party.me.meta
            data = (meta.get_prop('Default:AthenaCosmeticLoadout_j'))['AthenaCosmeticLoadout']

            try:
                data['cosmeticStats'][1]['statValue'] = amount
            except KeyError:
                data['cosmeticStats'] = [{"statName": "TotalVictoryCrowns", "statValue": amount},
                                        {"statName": "TotalRoyalRoyales", "statValue": amount},
                                        {"statName": "HasCrown", "statValue": 0}]

            final = {'AthenaCosmeticLoadout': data}
            key = 'Default:AthenaCosmeticLoadout_j'
            prop = {key: meta.set_prop(key, final)}

            await client.party.me.patch(updated=prop)
            await client.party.me.clear_emote()
            await client.party.me.set_emote('EID_Coronet')
            await message.reply("Emoteing Crowning Achievement!")

        if message.content.startswith("!skin "):
            # Extract the skin name from the message
            skin_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up skin by name or ID
            for skin in skins:
                if skin["name"].lower() == skin_input.lower() or skin["id"] == skin_input:
                    await client.party.me.set_outfit(skin["id"])
                    await message.reply(f"Skin set to {skin['name']}!")

        if message.content.startswith("!backpack "):
            # Extract the backpack name from the message
            backpack_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up backpack by name or ID
            for backpack in backpacks:
                if backpack["name"].lower() == backpack_input.lower() or backpack["id"] == backpack_input:
                    await client.party.me.set_backpack(backpack["id"])
                    await message.reply(f"Backpack  set to {backpack['name']}!")

        if message.content.startswith("!pickaxe "):
            # Extract the pickaxe name from the message
            pickaxe_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up pickaxe by name or ID
            for pickaxe in pickaxes:
                if pickaxe["name"].lower() == pickaxe_input.lower() or pickaxe["id"] == pickaxe_input:
                    await client.party.me.set_pickaxe(pickaxe["id"])
                    await message.reply(f"Pickaxe set to {pickaxe['name']}!")

        if message.content.startswith("!emote "):
            await client.party.me.clear_emote()
            # Extract the emote name from the message
            emote_input = " ".join(message.content.split(" ")[1:]).strip()

            # Look up emote by name or ID
            for emote in emotes:
                if emote["name"].lower() == emote_input.lower() or emote["id"] == emote_input:
                    await client.party.me.set_emote(emote["id"])
                    await message.reply(f"Emote set to {emote['name']}!")

        if message.content.lower().startswith('!level'):
            level = message.content.split(' ')[1]
            await client.party.me.set_banner(season_level=level)
            await message.reply(f"Level set to {level}!")

        if message.content.lower().startswith('!bp'):
            teir = message.content.split(' ')[1]
            await client.party.me.set_battlepass_info(
            has_purchased=True, level=teir)
            await message.reply(f"Teir set to {teir}!")

        if message.content.lower().startswith('!echo'):
            message = message.content.split(' ')[1]
            await client.party.send(message)

        if message.content.lower() == '!point':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_IceKing")
            await message.reply("Pointing out my pickaxe!")

        if message.content.lower().startswith('!privacy'):
            privacy = message.content.split(' ')[1]
            if privacy.lower() == 'public':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await message.reply("Privacy set to PUBLIC!")
            elif privacy.lower() == 'friends_allow_friends_of_friends':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply("Privacy set to FRIENDS_ALLOW_FRIENDS_OF_FRIENDS!")
            elif privacy.lower() == 'friends':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await message.reply("Privacy set to FRIENDS!")
            elif privacy.lower() == 'private_allow_friends_of_friends':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply("Privacy set to PRIVATE_ALLOW_FRIENDS_OF_FRIENDS!")
            elif privacy.lower() == 'private':
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await message.reply("Privacy set to PRIVATE!")
            else:
                await message.reply('Invalid privacy setting. Please use "public"/"friends_allow_friends_of_friends"/"friends"/"private_allow_friends_of_friends" or "private"!')

        if message.content.lower() == '!rareskins':
            await message.reply("Showing all Rare Skins!")
            purpleskull_skin_variants = client.party.me.create_variants(
                clothing_color=1
            )
            await client.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=purpleskull_skin_variants
        )
            await message.reply("Skin set to Purple Skull Trooper!")
            await asyncio.sleep(2)
            await client.party.me.set_outfit("CID_028_Athena_Commando_F")
            await message.reply("Skin set to Renegade Raider!")
            await asyncio.sleep(2)
            pinkghoul_skin_variants = client.party.me.create_variants(
                material=3
            )
            await client.party.me.set_outfit(
            asset='CID_029_Athena_Commando_F_Halloween',
            variants=pinkghoul_skin_variants
        )
            await message.reply("Skin set to Pink Ghoul Trooper!")
            await asyncio.sleep(2)
            await client.party.me.set_outfit("CID_017_Athena_Commando_M")
            await message.reply("Skin set to Aerial Assault Trooper!")
            await message.reply("Those are all of the Rare Skins!")

        if message.content.lower() == '!rarebackpacks':
            await message.reply("Showing all Rare Backpacks!")
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_140_StreetOpsMale")
            await message.reply("Backpack set to Response Unit!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_027_Scavenger")
            await message.reply("Backpack set to Rust Bucket!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_029_RetroGrey")
            await message.reply("Backpack set to Backup Plan!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_138_Celestial")
            await message.reply("Backpack set to Galactic Disc!")
            await asyncio.sleep(4)
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await asyncio.sleep(1)
            await client.party.me.set_backpack("BID_114_ModernMilitaryRed")
            await message.reply("Backpack set to Telemetry!")
            await message.reply("Those are all of the Rare Backpacks!")

        if message.content.lower() == '!rarepickaxes':
            await message.reply("Showing all Rare Pickaxes!")
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_376_FNCS")
            await message.reply("Pickaxe set to Axe Of Champions!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_069_DarkViking")
            await message.reply("Pickaxe set to Permafrost!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_Lockjaw")
            await message.reply("Pickaxe set to Raiders Revenge!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_189_StreetOpsStealth")
            await message.reply("Pickaxe set to Stealth Angular Axe!")
            await client.party.me.set_emote("EID_IceKing")
            await asyncio.sleep(8)
            await client.party.me.clear_emote()
            await client.party.me.set_pickaxe("Pickaxe_ID_075_Huya")
            await message.reply("Pickaxe set to Pointer!")
            await client.party.me.set_emote("EID_IceKing")
            await message.reply("Those are all of the Rare Pickaxe!")

        if message.content.lower() == '!rareemotes':
            await message.reply("Showing all Rare Emotes!")
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Fresh")
            await message.reply("Emote set to Fresh!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_AshtonBoardwalk")
            await message.reply("Emote set to Widow’s Pirouette!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_RunningManv3")
            await message.reply("Emote set to Pick It Up!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_TapShuffle")
            await message.reply("Emote set to Hootenanny!")
            await asyncio.sleep(4)
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_CycloneHeadBang")
            await message.reply("Emote set to Head Banger!")
            await message.reply("Those are all of the Rare Emotes!")

        if message.content.lower() == '!invite':
            # invite the user who sent the message
            member = await client.fetch_profile(message.author.id, cache=False, raw=False)
            await client.party.invite(member.id)
            await message.reply(f"Invited {member.display_name} to the party.")

        if message.content.startswith('!invite '):
            username = message.content[8:].strip()
            members = client.friends
            member = next((m for m in members if m.display_name.lower() == username.lower() or m.id == username), None)
            if member:
                await client.party.invite(member.id)
                await message.reply(f"Invited {member.display_name} to the party.")
            else:
                await message.reply("Could not find a member with that name or ID!")

        if message.content.lower() == '!stop':
            await client.party.me.clear_emote()
            await message.reply("Stoped emoteing!")

        if message.content.lower() == '!join':
            await message.reply("We're still working on this command! 😅")

        if message.content.startswith('!promote'):
            await message.reply("We're still working on this command! 😅")

        if message.content.lower() == '!kick':
            await message.reply("We're still working on this command! 😅")

        if message.content.lower() == '!leave':
            await message.reply("Leaveing the party!")
            await client.party.me.leave()

        if message.content.lower() == '!griddy':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Griddles")
            await message.reply("Emote set to Get Griddy")

        if message.content.lower() == '!purpleskull':
            purpleskull_skin_variants = client.party.me.create_variants(
                clothing_color=1
            )
            await client.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=purpleskull_skin_variants
        )
            await message.reply("Skin set to Purple Skull Trooper")

        if message.content.lower() == '!renegaderaider':
            await client.party.me.set_outfit("CID_028_Athena_Commando_F")
            await message.reply("Skin set to Renegade Raider")

        if message.content.lower() == '!pinkghoul':
            pinkghoul_skin_variants = client.party.me.create_variants(
                material=3
            )
            await client.party.me.set_outfit(
            asset='CID_029_Athena_Commando_F_Halloween',
            variants=pinkghoul_skin_variants
        )
            await message.reply("Skin set to Pink Ghoul Trooper")

        if message.content.lower() == '!aerial':
            await client.party.me.set_outfit("CID_017_Athena_Commando_M")
            await message.reply("Skin set to Aerial Assault Trooper")

        if message.content.lower() == '!ikonik':
            await client.party.me.set_outfit("CID_313_Athena_Commando_M_KpopFashion")
            await message.reply("Skin set to Ikonik")

        if message.content.lower() == '!ninja':
            await client.party.me.set_outfit("CID_605_Athena_Commando_M_TourBus")
            await message.reply("Skin set to Ninja")

        if message.content.lower() == "!hologram":
            await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
            await message.reply("Skin set to Hologram")

        if message.content.lower().startswith("!gift"):
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_NeverGonna")
            await message.reply("Nice try but I can't gift!")

        if message.content.lower() == "!tbd":
            response = requests.get("https://package.lobbybots.ga/skins")
            data = response.json()
            await message.reply("Showing all TBD skins!")

            for item in data:
                if item.get("name") == "TBD":
                    skin_name = item.get("name")
                    await client.party.me.set_outfit(item.get("id"))
                    await message.reply(f"Skin set to {skin_name}")
                    await asyncio.sleep(2)

            await message.reply("Those are all of the TBD skins!")

        if message.content.lower() == '!shop':
            await message.reply("We're still working on this command! 😅")

        if message.content.lower() == '!hatlessrecon':
            skin_variants = client.party.me.create_variants(
                parts=2
            )

            await client.party.me.set_outfit(
                asset='CID_022_Athena_Commando_F',
                variants=skin_variants
            )
            await message.reply("Skin set to Recon Expert!")

        if message.content.lower() == '!henchman':
            random_henchman = random.choice(
                [
                    "CID_794_Athena_Commando_M_HenchmanBadShorts_D",
                    "CID_NPC_Athena_Commando_F_HenchmanSpyDark",
                    "CID_791_Athena_Commando_M_HenchmanGoodShorts_D",
                    "CID_780_Athena_Commando_M_HenchmanBadShorts",
                    "CID_NPC_Athena_Commando_M_HenchmanGood",
                    "CID_692_Athena_Commando_M_HenchmanTough",
                    "CID_707_Athena_Commando_M_HenchmanGood",
                    "CID_792_Athena_Commando_M_HenchmanBadShorts_B",
                    "CID_793_Athena_Commando_M_HenchmanBadShorts_C",
                    "CID_NPC_Athena_Commando_M_HenchmanBad",
                    "CID_790_Athena_Commando_M_HenchmanGoodShorts_C",
                    "CID_779_Athena_Commando_M_HenchmanGoodShorts",
                    "CID_NPC_Athena_Commando_F_RebirthDefault_Henchman",
                    "CID_NPC_Athena_Commando_F_HenchmanSpyGood",
                    "CID_706_Athena_Commando_M_HenchmanBad",
                    "CID_789_Athena_Commando_M_HenchmanGoodShorts_B"
                ]
            )

            await client.party.me.set_outfit(
                asset=random_henchman
            )
            await message.reply("Skin set to a random henchman!")

        if message.content.lower() == '!marauder':
            random_marauder = random.choice(
                [
                    "CID_NPC_Athena_Commando_M_MarauderHeavy",
                    "CID_NPC_Athena_Commando_M_MarauderElite",
                    "CID_NPC_Athena_Commando_M_MarauderGrunt"
                ]
            )

            await client.party.me.set_outfit(
                asset=random_marauder
            )
            await message.reply("Skin set to a random marauder!")

        if message.content.lower() == '!goldenbrutus':
            await client.party.me.set_outfit(
                asset='CID_692_Athena_Commando_M_HenchmanTough',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 180)
            )
            await message.reply("Skin set to Golden Brutus!")

        if message.content.lower() == '!goldenmeowscles':
            await client.party.me.set_outfit(
                asset='CID_693_Athena_Commando_M_BuffCat',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 220)
            )
            await message.reply("Skin set to Golden Meowscles!")

        if message.content.lower() == '!goldenmidas':
            await client.party.me.set_outfit(
                asset='CID_694_Athena_Commando_M_CatBurglar',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 140)
            )
            await message.reply("Skin set to Golden Midas!")

        if message.content.lower() == '!goldenskye':
            await client.party.me.set_outfit(
                asset='CID_690_Athena_Commando_F_Photographer',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 300)
            )
            await message.reply("Skin set to Golden Skye!")

        if message.content.lower() == '!goldenpeely':
            await client.party.me.set_outfit(
                asset='CID_701_Athena_Commando_M_BananaAgent',
                variants=client.party.me.create_variants(progressive=4),
                enlightenment=(2, 350)
            )
            await message.reply("Skin set to Golden Peely!")
            
        if message.content.lower() == '!goldentntina':
            await client.party.me.set_outfit(
                asset='CID_691_Athena_Commando_F_TNTina',
                variants=client.party.me.create_variants(progressive=7),
                enlightenment=(2, 260)
            )
            await message.reply("Skin set to Golden TNTina!")
            
        if message.content.lower() == '!checkerredrenegade':
            skin_variants = client.party.me.create_variants(
                material=2
            )

            await client.party.me.set_outfit(
                asset='CID_028_Athena_Commando_F',
                variants=skin_variants
            )
            await message.reply("Skin set to Renegade Raider!")

        if message.content.lower() == '!mintyelf':
            skin_variants = client.party.me.create_variants(
                material=2
            )

            await client.party.me.set_outfit(
                asset='CID_051_Athena_Commando_M_HolidayElf',
                variants=skin_variants
            )
            await message.reply("Skin set to Minty Elf!")

        if message.content.lower() == '!floss':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Floss")
            await message.reply("Emote set to Floss!")

        if message.content.lower() == '!scenario':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_KPopDance03")
            await message.reply("Emote set to Scenario!")

        if message.content.lower() == '!wave':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_Wave")
            await message.reply("Emote set to Wave!")

        if message.content.lower() == '!ponpon':
            await client.party.me.clear_emote()
            await client.party.me.set_emote("EID_TourBus")
            await message.reply("Emote set to Ninja Style")

        if message.content.lower() == '!nobackpack':
            await client.party.me.clear_backpack()
            await message.reply("Removed Backpack!")

        if message.content.lower() == '!nopet':
            await client.party.me.clear_pet()
            await message.reply("Removed Pet!")

        if message.content.lower() == '!purpleportal':
            skin_variants = client.party.me.create_variants(
                config_overrides={
                    'particle': 'Particle{}'
                },
                particle=1
            )
            await client.party.me.set_backpack(
                asset='BID_105_GhostPortal',
                variants=skin_variants
            )
            await message.reply("Backpack set to Ghost Portal!")

        if message.content.startswith('!copy'):
            epic_username = message.content.split(' ')[1] if len(message.content.split(' ')) > 1 else None
            
            if epic_username is None:
                member = [m for m in client.party.members if m.id == message.author.id][0]
            else:
                user = await client.fetch_user(epic_username)
                member = [m for m in client.party.members if m.id == user.id][0]

            await client.party.me.edit(
                functools.partial(
                    fortnitepy.ClientPartyMember.set_outfit,
                    asset=member.outfit,
                    variants=member.outfit_variants
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_backpack,
                    asset=member.backpack,
                    variants=member.backpack_variants
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_pickaxe,
                    asset=member.pickaxe,
                    variants=member.pickaxe_variants
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_banner,
                    icon=member.banner[0],
                    color=member.banner[1],
                    season_level=member.banner[2]
                ),
                functools.partial(
                    fortnitepy.ClientPartyMember.set_battlepass_info,
                    has_purchased=True,
                    level=member.battlepass_info[1]
                )
            )

            if member.emote is not None:
                await client.party.me.set_emote(asset=member.emote)

            await message.reply(f'Copied the loadout of {member.display_name}.')

        if message.content.startswith('!variants'):
            args = re.findall(r'"[^"]+"|\S+', message.content)[1:]
            if len(args) < 3:
                await message.reply('Usage: !variants "<cosmetic_id>" <variant_type> <variant_index>')
                return

            cosmetic_id = args[0].strip('"')
            variant_type = args[1]
            variant_index = args[2]

            if not variant_index.isdigit():
                await message.reply('Variant index must be a number.')
                return

            if 'cid' in cosmetic_id.lower() and 'jersey_color' not in variant_type.lower():
                skin_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=skin_variants
                )

            elif 'cid' in cosmetic_id.lower() and 'jersey_color' in variant_type.lower():
                cosmetic_variants = client.party.me.create_variants(
                    pattern=0,
                    numeric=69,
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            elif 'bid' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_backpack(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )
            elif 'pickaxe_id' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_pickaxe(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            else:
                await message.reply(f'Invalid cosmetic ID: {cosmetic_id}')

        if message.content.startswith('!style'):
            args = re.findall(r'"[^"]+"|\S+', message.content)[1:]
            if len(args) < 3:
                await message.reply('Usage: !style "<cosmetic_id>" <variant_type> <variant_index>')
                return

            cosmetic_id = args[0].strip('"')
            variant_type = args[1]
            variant_index = args[2]

            if not variant_index.isdigit():
                await message.reply('Variant index must be a number.')
                return

            if 'cid' in cosmetic_id.lower() and 'jersey_color' not in variant_type.lower():
                skin_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=skin_variants
                )

            elif 'cid' in cosmetic_id.lower() and 'jersey_color' in variant_type.lower():
                cosmetic_variants = client.party.me.create_variants(
                    pattern=0,
                    numeric=69,
                    **{variant_type: variant_index}
                )

                await client.party.me.set_outfit(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            elif 'bid' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_backpack(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )
            elif 'pickaxe_id' in cosmetic_id.lower():
                cosmetic_variants = client.party.me.create_variants(
                    **{variant_type: variant_index}
                )

                await client.party.me.set_pickaxe(
                    asset=cosmetic_id,
                    variants=cosmetic_variants
                )

            else:
                await message.reply(f'Invalid cosmetic ID: {cosmetic_id}')

        if message.content.lower() == "!new skins":
            response = requests.get("https://package.lobbybots.ga/new/skins")
            data = response.json()

            if not data:
                await message.reply("Theres no new skins!")
            else:
                for item in data:
                    skin_name = item.get("name")
                    await message.reply("Showing all new skins!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_outfit(item.get("id"))
                    await message.reply(f"Skin set to {skin_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower() == "!new backpacks":
            response = requests.get("https://package.lobbybots.ga/new/backpacks")
            data = response.json()

            if not data:
                await message.reply("Theres no new backpacks!")
            else:
                for item in data:
                    backpack_name = item.get("name")
                    await message.reply("Showing all new backpacks!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_outfit("CID_VIP_Athena_Commando_M_GalileoGondola_SG")
                    await client.party.me.set_backpack(item.get("id"))
                    await message.reply(f"Backpack set to {backpack_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower() == "!new pickaxes":
            response = requests.get("https://package.lobbybots.ga/new/pickaxes")
            data = response.json()

            if not data:
                await message.reply("Theres no new pickaxes!")
            else:
                for item in data:
                    pickaxe_name = item.get("name")
                    await message.reply("Showing all new pickaxes!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_pickaxe(item.get("id"))
                    await client.party.me.set_emote("EID_IceKing")
                    await message.reply(f"Pickaxe set to {pickaxe_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower() == "!new emotes":
            response = requests.get("https://package.lobbybots.ga/new/emotes")
            data = response.json()

            if not data:
                await message.reply("Theres no new emotes!")
            else:
                for item in data:
                    emote_name = item.get("name")
                    await message.reply("Showing all new emotes!")
                    await client.party.me.clear_emote()
                    await client.party.me.set_emote(item.get("id"))
                    await message.reply(f"Emote set to {emote_name}")
                    await asyncio.sleep(8)

                await message.reply("Thats it for now!")

        if message.content.lower().startswith('!random'):
            item = message.content.split(' ')[1]
            if item.lower() == 'skin':
                skin_response = requests.get('https://package.lobbybots.ga/skins')
                skin_data = random.choice(skin_response.json())
                await client.party.me.set_outfit(f"{skin_data['id']}")
                await message.reply(f"Skin set to: {skin_data['name']}")
            elif item.lower() == 'backpack':
                backpack_response = requests.get('https://package.lobbybots.ga/backpacks')
                backpack_data = random.choice(backpack_response.json())
                await client.party.me.set_backpack(f"{backpack_data['id']}")
                await message.reply(f"Backpack set to: {backpack_data['name']}")
            elif item.lower() == 'pickaxe':
                pickaxe_response = requests.get('https://package.lobbybots.ga/pickaxes')
                pickaxe_data = random.choice(pickaxe_response.json())
                await client.party.me.set_pickaxe(f"{pickaxe_data['id']}")
                await client.party.me.clear_emote()
                await client.party.me.set_emote("EID_IceKing")
                await message.reply(f"Pickaxe set to: {pickaxe_data['name']}")
            elif item.lower() == 'emote':
                await client.party.me.clear_emote()
                emote_response = requests.get('https://package.lobbybots.ga/emotes')
                emote_data = random.choice(emote_response.json())
                await client.party.me.set_emote(f"{emote_data['id']}")
                await message.reply(f"Emote set to: {emote_data['name']}")
            elif item.lower() == 'all':
                await client.party.me.clear_emote()
                skin_response = requests.get('https://package.lobbybots.ga/skins')
                backpack_response = requests.get('https://package.lobbybots.ga/backpacks')
                pickaxe_response = requests.get('https://package.lobbybots.ga/pickaxes')
                emote_response = requests.get('https://package.lobbybots.ga/emotes')
                skin_data = random.choice(skin_response.json())
                backpack_data = random.choice(backpack_response.json())
                pickaxe_data = random.choice(pickaxe_response.json())
                emote_data = random.choice(emote_response.json())
                await client.party.me.set_outfit(f"{skin_data['id']}")
                await client.party.me.set_backpack(f"{backpack_data['id']}")
                await client.party.me.set_pickaxe(f"{pickaxe_data['id']}")
                await client.party.me.set_emote(f"{emote_data['id']}")
                await message.reply(f"Skin set to: {skin_data['name']}.\nBackpack set to: {backpack_data['name']}.\nPickaxe set to: {pickaxe_data['name']}.\nEmote set to: {emote_data['name']}.")
            else:
                await message.reply("Invalid! Please user !random skin/backpack/pickaxe/emote/all.")

    with open(config_file, 'r') as f:
        config = json.load(f)

    auto_update = str(config.get('auto_update', False))

    if auto_update == 'True':
        print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + 'Updating packages...' + '\033[0m')
        os.system("pip install --upgrade fortnitepy > /dev/null 2>&1; pip install --upgrade testlobby > /dev/null 2>&1")
        print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + 'Done!' + '\033[0m')
    else:
        print('\033[36m' + "[FnLobbyBot] " + '\033[97m' + 'Auto update is disabled. (Not recommended)' + '\033[0m')

    # Start the client
    try:
        client.run()
    except Exception:
        print('\033[36m' + "[FnLobbyBot] " + '\033[31m' + "Can't login because your device auths are wrong." + '\033[0m')
        print('\033[36m' + "[FnLobbyBot] " + '\033[36m' + "Video tutorial: https://youtube.com." + '\033[0m')
        print('\033[36m' + "[FnLobbyBot] " + '\033[36m' + "Login to the account you want the bot to use and go to this website https://lobbybots.ga/authcode and code the authorizationCode only! " + '\033[31m' + "IF THE AUTH CODE SAYS NULL THEN YOU NEED TO LOGIN TO THE ACCOUNT AGAIN!" + '\033[0m')
        print('\033[36m' + "[FnLobbyBot] " + '\033[31m' + "DONT USE YOUR MAIN ACCOUNT!" + '\033[0m')
        auth_code = input('\033[36m' + "[FnLobbyBot] " + '\033[97m' + 'Enter your authorizationCode: ' + '\033[0m')

        # Send a POST request to the website with the auth code
        response = requests.post("http://authorization.lobbybots.ga/get_auth", data={"auth_code": auth_code})

        # Check if the response is successful
        if response.status_code == 200:
            # If the response is successful, print the device ID, account ID, and secret
            data = response.json()
            device_id = data["device_id"]
            account_id = data["account_id"]
            secret = data["secret"]
            print('\033[36m' + "[FnLobbyBot] " + '\033[32m' + "Device Auths saved! Restart the project to get your bot online!"+ '\033[0m')

            # Save the device ID, account ID, and secret to a file
            device_auth = [{"device_id": device_id, "account_id": account_id, "secret": secret}]
            with open(device_auth_file, "w") as f:
                json.dump(device_auth, f)
        else:
            # If the response is not successful, print an error message
            print('\033[36m' + "[FnLobbyBot] " + '\033[31m' + "Error processing auth code please try again later." + '\033[0m')