# DvZ
Resource pack for DvZ 1.19.2

## Language Edits
The following Changes have been made to the main English language files (`en_au`, `en_ca`, `en_gb`, `en_us`):
| key                                     | original (`en_us`)  | custom                |
|-----------------------------------------|---------------------|-----------------------|
| `soundCategory.ambient`                 | Ambient/Environment | Hero Warnings/Events* |
| `soundCategory.block`                   | Blocks              | Blocks                |
| `soundCategory.hostile`                 | Hostile Creatures   | Mobs*                 |
| `soundCategory.master`                  | Master Volume       | Master Volume         |
| `soundCategory.music`                   | Music               | Minecraft Music*      |
| `soundCategory.neutral`                 | Friendly Creatures  | DvZ Music*            |
| `soundCategory.player`                  | Players             | Jimmies*              |
| `soundCategory.record`                  | Jukebox/Note Blocks | Heroes Messages*      |
| `soundCategory.voice`                   | Voice/Speech        | Voice/Speech          |
| `soundCategory.weather`                 | Weather             | Tools/Crafting*       |
| `item.minecraft.music_disc_NAME.desc`   | Disc name           | *                     |
| `instrument.minecraft.ponder_goat_horn` | Ponder              | *                     |
*: Edited

## Sounds
The following default sounds have been removed:
- `ambient.cave`
- `weather.rain`
- `weather.rain.above`
- `entity.player.death`
- `entity.villager.ambient`
- `music.game`
- `music.creative`
- `music.end`
- `music.credits`
- `music.dragon`
- `music.nether.basalt_deltas`
- `music.nether.crimson_forest`
- `music.nether.nether_wastes`
- `music.nether.soul_sand_valley`
- `music.nether.warped_forest`
- `music.overworld.deep_dark`
- `music.overworld.dripstone_caves`
- `music.overworld.frozen_peaks`
- `music.overworld.grove`
- `music.overworld.jagged_peaks`
- `music.overworld.jungle_and_forest`
- `music.overworld.lush_caves`
- `music.overworld.meadow`
- `music.overworld.old_growth_taiga`
- `music.overworld.snowy_slopes`
- `music.overworld.stony_peaks`
- `music.overworld.swamp`
- `music.under_water`
- `item.goat_horn.sound.0`

The following default sounds have been replaced by custom sounds:
- [`entity.arrow.shoot`](assets/minecraft/sounds/random/bow.ogg?raw=true)
- [`entity.skeleton.shoot`](assets/minecraft/sounds/random/bow.ogg?raw=true)
- [`entity.arrow.hit`](assets/minecraft/sounds/random/bowhit1.ogg?raw=true)

The following custom sounds have been added:
| key                                                                                                                 | intended category |
|---------------------------------------------------------------------------------------------------------------------|-------------------|
| [`activatebow`](assets/minecraft/sounds/activatebow.ogg?raw=true)                                                   | `weather`         |
| [`activateshield`](assets/minecraft/sounds/activateshield.ogg?raw=true)                                             | `weather`         |
| [`activatesword`](assets/minecraft/sounds/activatesword.ogg?raw=true)                                               | `weather`         |
| [`toolaxehit`](assets/minecraft/sounds/toolaxehit1.ogg?raw=true)                                                    | `weather`         |
| [`toolwoodchop`](assets/minecraft/sounds/toolwoodchop1.ogg?raw=true)                                                | `weather`         |
| [`wpnmonstersmash`](assets/minecraft/sounds/wpnmonstersmash1.ogg?raw=true)                                          | `weather`         |
| [`wpnmonstersmashbig`](assets/minecraft/sounds/wpnmonstersmashbig1.ogg?raw=true)                                    | `weather`         |
| [`wpnwarhammer`](assets/minecraft/sounds/wpnwarhammer1.ogg?raw=true)                                                | `weather`         |
| [`wpncrossbow`](assets/minecraft/sounds/wpncrossbow1.ogg?raw=true)                                                  | `weather`         |
| [`emeraldbowfire`](assets/minecraft/sounds/emeraldbowfire1.ogg?raw=true)                                            | `weather`         |
| [`emeraldbowdraw`](assets/minecraft/sounds/emeraldbowdraw.ogg?raw=true)                                             | `weather`         |
| [`hatgoggles`](assets/minecraft/sounds/hatgoggles1.ogg?raw=true)                                                    | `sound`           |
| [`hatdragonwarrior`](assets/minecraft/sounds/hatdragonwarrior.ogg?raw=true)                                         | `sound`           |
| [`hatdragonsbreath`](assets/minecraft/sounds/hatdragonsbreath.ogg?raw=true)                                         | `sound`           |
| [`hatpharaoh`](assets/minecraft/sounds/hatpharaoh.ogg?raw=true)                                                     | `sound`           |
| [`hatsunglasses`](assets/minecraft/sounds/hatsunglasses.ogg?raw=true)                                               | `sound`           |
| [`hatwolfhunter`](assets/minecraft/sounds/hatwolfhunter.ogg?raw=true)                                               | `sound`           |
| [`general.offcooldown`](assets/minecraft/sounds/general.offcooldown.ogg?raw=true)                                   | `sound`           |
| [`doomeventbarnyard`](assets/minecraft/sounds/doomeventbarnyard.ogg?raw=true)                                       | `ambient`         |
| [`doomeventbopen`](assets/minecraft/sounds/doomeventbopen.ogg?raw=true)                                             | `ambient`         |
| [`doomeventkrungor`](assets/minecraft/sounds/doomeventkrungor.ogg?raw=true)                                         | `ambient`         |
| [`doomevent1`](assets/minecraft/sounds/doomevent1.ogg?raw=true)                                                     | `ambient`         |
| [`doomevent2`](assets/minecraft/sounds/doomevent2.ogg?raw=true)                                                     | `ambient`         |
| [`doomevent3`](assets/minecraft/sounds/doomevent3.ogg?raw=true)                                                     | `ambient`         |
| [`doomevent4`](assets/minecraft/sounds/doomevent4.ogg?raw=true)                                                     | `ambient`         |
| [`doomevent5`](assets/minecraft/sounds/doomevent5.ogg?raw=true)                                                     | `ambient`         |
| [`wpnwarpweaver`](assets/minecraft/sounds/wpnwarpweaver.ogg?raw=true)                                               | `weather`         |
| [`wpnplunder`](assets/minecraft/sounds/wpnplunder.ogg?raw=true)                                                     | `weather`         |
| [`wind`](assets/minecraft/sounds/wind.ogg?raw=true)                                                                 | `sounds`          |
| [`wpnsos`](assets/minecraft/sounds/wpnsos.ogg?raw=true)                                                             | `ambient`         |
| [`magiccoil`](assets/minecraft/sounds/magiccoil.ogg?raw=true)                                                       | `ambient`         |
| [`wpnbuffalohorn`](assets/minecraft/sounds/wpnbuffalohorn.ogg?raw=true)                                             | `ambient`         |
| [`wpnproc`](assets/minecraft/sounds/wpnproc.ogg?raw=true)                                                           | `ambient`         |
| [`general.hitding`](assets/minecraft/sounds/general.hitding.ogg?raw=true)                                           | `sounds`          |
| [`warhammercharge`](assets/minecraft/sounds/warhammercharge.ogg?raw=true)                                           | `ambient`         |
| [`warhammerrankup`](assets/minecraft/sounds/warhammerrankup.ogg?raw=true)                                           | `ambient`         |
| [`runebladerunedash`](assets/minecraft/sounds/runebladerunedash.ogg?raw=true)                                       | `ambient`         |
| [`wpnenchantedlamp`](assets/minecraft/sounds/wpnenchantedlamp.ogg?raw=true)                                         | `weather`         |
| [`coin`](assets/minecraft/sounds/misc/coin.ogg?raw=true)                                                            | `player`          |
| [`coinflip`](assets/minecraft/sounds/misc/coinflip.ogg?raw=true)                                                    | `player`          |
| [`brucecasual1`](assets/minecraft/sounds/brucecasual1.ogg?raw=true)                                                 | `record`          |
| [`brucecombatgeneral1`](assets/minecraft/sounds/brucecombatgeneral1.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral2`](assets/minecraft/sounds/brucecombatgeneral2.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral3`](assets/minecraft/sounds/brucecombatgeneral3.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral4`](assets/minecraft/sounds/brucecombatgeneral4.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral5`](assets/minecraft/sounds/brucecombatgeneral5.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral6`](assets/minecraft/sounds/brucecombatgeneral6.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral7`](assets/minecraft/sounds/brucecombatgeneral7.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral8`](assets/minecraft/sounds/brucecombatgeneral8.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral9`](assets/minecraft/sounds/brucecombatgeneral9.ogg?raw=true)                                   | `record`          |
| [`brucecombatgeneral10`](assets/minecraft/sounds/brucecombatgeneral10.ogg?raw=true)                                 | `record`          |
| [`brucecombatgeneral11`](assets/minecraft/sounds/brucecombatgeneral11.ogg?raw=true)                                 | `record`          |
| [`brucecombatgeneral12`](assets/minecraft/sounds/brucecombatgeneral12.ogg?raw=true)                                 | `record`          |
| [`brucecombatgeneral13`](assets/minecraft/sounds/brucecombatgeneral13.ogg?raw=true)                                 | `record`          |
| [`brucecombatindoors1`](assets/minecraft/sounds/brucecombatindoors1.ogg?raw=true)                                   | `record`          |
| [`brucecombatindoors2`](assets/minecraft/sounds/brucecombatindoors2.ogg?raw=true)                                   | `record`          |
| [`brucecombatindoors3`](assets/minecraft/sounds/brucecombatindoors3.ogg?raw=true)                                   | `record`          |
| [`brucecombatindoors4`](assets/minecraft/sounds/brucecombatindoors4.ogg?raw=true)                                   | `record`          |
| [`brucecombatoutdoors1`](assets/minecraft/sounds/brucecombatoutdoors1.ogg?raw=true)                                 | `record`          |
| [`brucecombatoutdoors2`](assets/minecraft/sounds/brucecombatoutdoors2.ogg?raw=true)                                 | `record`          |
| [`brucecombatoutdoors3`](assets/minecraft/sounds/brucecombatoutdoors3.ogg?raw=true)                                 | `record`          |
| [`brucecombatoutdoors4`](assets/minecraft/sounds/brucecombatoutdoors4.ogg?raw=true)                                 | `record`          |
| [`brucecombatoutdoors5`](assets/minecraft/sounds/brucecombatoutdoors5.ogg?raw=true)                                 | `record`          |
| [`bruceexplosionnearby1`](assets/minecraft/sounds/bruceexplosionnearby1.ogg?raw=true)                               | `record`          |
| [`bruceexplosionnearby2`](assets/minecraft/sounds/bruceexplosionnearby2.ogg?raw=true)                               | `record`          |
| [`brucedeath`](assets/minecraft/sounds/brucedeath.ogg?raw=true)                                                     | `ambient`         |
| [`brucediggingzombiewarning`](assets/minecraft/sounds/brucediggingzombiewarning.ogg?raw=true)                       | `ambient`         |
| [`brucegolemwarning`](assets/minecraft/sounds/brucegolemwarning1.ogg?raw=true)                                      | `ambient`         |
| [`bruceintro`](assets/minecraft/sounds/bruceintro.ogg?raw=true)                                                     | `ambient`         |
| [`brucelowonmana1`](assets/minecraft/sounds/brucelowonmana1.ogg?raw=true)                                           | `record`          |
| [`brucelowonmana2`](assets/minecraft/sounds/brucelowonmana2.ogg?raw=true)                                           | `record`          |
| [`brucelowonmana3`](assets/minecraft/sounds/brucelowonmana3.ogg?raw=true)                                           | `record`          |
| [`bruceproc1`](assets/minecraft/sounds/bruceproc1.ogg?raw=true)                                                     | `record`          |
| [`bruceproc2`](assets/minecraft/sounds/bruceproc2.ogg?raw=true)                                                     | `record`          |
| [`bruceproc3`](assets/minecraft/sounds/bruceproc3.ogg?raw=true)                                                     | `record`          |
| [`bruceproc`](assets/minecraft/sounds/bruceproc1.ogg?raw=true)                                                      | `ambient`         |
| [`bruceratswarning`](assets/minecraft/sounds/bruceratswarning1.ogg?raw=true)                                        | `ambient`         |
| [`bruceshrinedestroyed1`](assets/minecraft/sounds/bruceshrinedestroyed1.ogg?raw=true)                               | `ambient`         |
| [`bruceshrinedestroyed2`](assets/minecraft/sounds/bruceshrinedestroyed2.ogg?raw=true)                               | `ambient`         |
| [`bruceshrinedestroyed3`](assets/minecraft/sounds/bruceshrinedestroyed3.ogg?raw=true)                               | `ambient`         |
| [`brucespideringswarning`](assets/minecraft/sounds/brucespideringswarning1.ogg?raw=true)                            | `ambient`         |
| [`brucevenomburnerswarning`](assets/minecraft/sounds/brucevenomburnerswarning1.ogg?raw=true)                        | `ambient`         |
| [`brucewolveswarning`](assets/minecraft/sounds/brucewolveswarning1.ogg?raw=true)                                    | `ambient`         |
| [`brucemonstersreleased`](assets/minecraft/sounds/brucemonstersreleased.ogg?raw=true)                               | `ambient`         |
| [`brucenoprocwarning`](assets/minecraft/sounds/brucenoprocwarning1.ogg?raw=true)                                    | `ambient`         |
| [`brucenomanawarning`](assets/minecraft/sounds/brucenomanawarning1.ogg?raw=true)                                    | `ambient`         |
| [`brucenorepairwarning`](assets/minecraft/sounds/brucenorepairwarning1.ogg?raw=true)                                | `ambient`         |
| [`maliceintro`](assets/minecraft/sounds/maliceintro.ogg?raw=true)                                                   | `ambient`         |
| [`malicegeneral`](assets/minecraft/sounds/malicegeneral1.ogg?raw=true)                                              | `record`          |
| [`maliceuse`](assets/minecraft/sounds/maliceuse1.ogg?raw=true)                                                      | `record`          |
| [`daragorattack`](assets/minecraft/sounds/daragorattack1.ogg?raw=true)                                              | `ambient`         |
| [`daragordeath`](assets/minecraft/sounds/daragordeath.ogg?raw=true)                                                 | `ambient`         |
| [`daragorspawn`](assets/minecraft/sounds/daragorspawn.ogg?raw=true)                                                 | `ambient`         |
| [`daragortaunt`](assets/minecraft/sounds/daragortaunt1.ogg?raw=true)                                                | `ambient`         |
| [`daragorworldcracker`](assets/minecraft/sounds/daragorworldcracker1.ogg?raw=true)                                  | `ambient`         |
| [`dvzlore1`](assets/minecraft/sounds/dvzlore1.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore2`](assets/minecraft/sounds/dvzlore2.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore3`](assets/minecraft/sounds/dvzlore3.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore4`](assets/minecraft/sounds/dvzlore4.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore5`](assets/minecraft/sounds/dvzlore5.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore6`](assets/minecraft/sounds/dvzlore6.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore7`](assets/minecraft/sounds/dvzlore7.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore8`](assets/minecraft/sounds/dvzlore8.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore9`](assets/minecraft/sounds/dvzlore9.ogg?raw=true)                                                         | `neutral`         |
| [`dvzlore10`](assets/minecraft/sounds/dvzlore10.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore11`](assets/minecraft/sounds/dvzlore11.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore12`](assets/minecraft/sounds/dvzlore12.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore13`](assets/minecraft/sounds/dvzlore13.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore14`](assets/minecraft/sounds/dvzlore14.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore15`](assets/minecraft/sounds/dvzlore15.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore16`](assets/minecraft/sounds/dvzlore16.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore17`](assets/minecraft/sounds/dvzlore17.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore18`](assets/minecraft/sounds/dvzlore18.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore19`](assets/minecraft/sounds/dvzlore19.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore20`](assets/minecraft/sounds/dvzlore20.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore21`](assets/minecraft/sounds/dvzlore21.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore22`](assets/minecraft/sounds/dvzlore22.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore23`](assets/minecraft/sounds/dvzlore23.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore24`](assets/minecraft/sounds/dvzlore24.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore25`](assets/minecraft/sounds/dvzlore25.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore26`](assets/minecraft/sounds/dvzlore26.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore27`](assets/minecraft/sounds/dvzlore27.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore28`](assets/minecraft/sounds/dvzlore28.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore29`](assets/minecraft/sounds/dvzlore29.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore30`](assets/minecraft/sounds/dvzlore30.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore31`](assets/minecraft/sounds/dvzlore31.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore32`](assets/minecraft/sounds/dvzlore32.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore33`](assets/minecraft/sounds/dvzlore33.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore34`](assets/minecraft/sounds/dvzlore34.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore35`](assets/minecraft/sounds/dvzlore35.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore36`](assets/minecraft/sounds/dvzlore36.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore37`](assets/minecraft/sounds/dvzlore37.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore38`](assets/minecraft/sounds/dvzlore38.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore39`](assets/minecraft/sounds/dvzlore39.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore40`](assets/minecraft/sounds/dvzlore40.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore41`](assets/minecraft/sounds/dvzlore41.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore42`](assets/minecraft/sounds/dvzlore42.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore43`](assets/minecraft/sounds/dvzlore43.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore44`](assets/minecraft/sounds/dvzlore44.ogg?raw=true)                                                       | `neutral`         |
| [`dvzlore45`](assets/minecraft/sounds/dvzlore45.ogg?raw=true)                                                       | `neutral`         |
| [`daragorfirebreath`](assets/minecraft/sounds/daragorfirebreath1.ogg?raw=true)                                      | `ambient`         |
| [`introsong`](assets/minecraft/sounds/introsong.ogg?raw=true)                                                       | `neutral`         |
| [`nisovin.rocketboots`](assets/minecraft/sounds/nisovin.rocketboots.ogg?raw=true)                                   | `weather`         |
| [`nisovin.voicewormhole`](assets/minecraft/sounds/nisovin.voicewormhole.ogg?raw=true)                               | `hostile`         |
| [`nisovin.wandfire`](assets/minecraft/sounds/nisovin.wandfire.ogg?raw=true)                                         | `weather`         |
| [`nisovin.wandhit`](assets/minecraft/sounds/nisovin.wandhit.ogg?raw=true)                                           | `weather`         |
| [`nisovin.wormholeactivate`](assets/minecraft/sounds/nisovin.wormholeactivate.ogg?raw=true)                         | `weather`         |
| [`nisovin.wormholefire`](assets/minecraft/sounds/nisovin.wormholefire.ogg?raw=true)                                 | `weather`         |
| [`nisovin.tinderflamedraw`](assets/minecraft/sounds/nisovin.tinderflamedraw.ogg?raw=true)                           | `weather`         |
| [`nisovin.tinderflame`](assets/minecraft/sounds/nisovin.tinderflame1.ogg?raw=true)                                  | `weather`         |
| [`nisovin.voicerocketboots`](assets/minecraft/sounds/nisovin.voicerocketboots1.ogg?raw=true)                        | `hostile`         |
| [`nisovin.voicetinderflame`](assets/minecraft/sounds/nisovin.voicetinderflame1.ogg?raw=true)                        | `hostile`         |
| [`nisovinboltfire`](assets/minecraft/sounds/nisovinboltfire1.ogg?raw=true)                                          | `weather`         |
| [`nisovindeath`](assets/minecraft/sounds/nisovindeath.ogg?raw=true)                                                 | `ambient`         |
| [`nisovinlaugh`](assets/minecraft/sounds/nisovinlaugh1.ogg?raw=true)                                                | `record`          |
| [`nisovinlowonmana1`](assets/minecraft/sounds/nisovinlowonmana1.ogg?raw=true)                                       | `ambient`         |
| [`nisovinlowonmana2`](assets/minecraft/sounds/nisovinlowonmana2.ogg?raw=true)                                       | `ambient`         |
| [`nisovinlowonmana3`](assets/minecraft/sounds/nisovinlowonmana3.ogg?raw=true)                                       | `ambient`         |
| [`roamindeath`](assets/minecraft/sounds/roamindeath.ogg?raw=true)                                                   | `ambient`         |
| [`roaminflamethrower`](assets/minecraft/sounds/roaminflamethrower.ogg?raw=true)                                     | `weather`         |
| [`roaminheal`](assets/minecraft/sounds/roaminheal.ogg?raw=true)                                                     | `roaminheal`      |
| [`roaminholypurifier1`](assets/minecraft/sounds/roaminholypurifier1.ogg?raw=true)                                   | `record`          |
| [`roaminholypurifier2`](assets/minecraft/sounds/roaminholypurifier2.ogg?raw=true)                                   | `record`          |
| [`roaminholypurifier3`](assets/minecraft/sounds/roaminholypurifier3.ogg?raw=true)                                   | `record`          |
| [`roaminholypurifier4`](assets/minecraft/sounds/roaminholypurifier4.ogg?raw=true)                                   | `record`          |
| [`roaminholypurifier5`](assets/minecraft/sounds/roaminholypurifier5.ogg?raw=true)                                   | `record`          |
| [`roaminlowonarmor1`](assets/minecraft/sounds/roaminlowonarmor1.ogg?raw=true)                                       | `ambient`         |
| [`roaminlowonarmor2`](assets/minecraft/sounds/roaminlowonarmor2.ogg?raw=true)                                       | `ambient`         |
| [`roaminlowonarmor3`](assets/minecraft/sounds/roaminlowonarmor3.ogg?raw=true)                                       | `ambient`         |
| [`roaminlowonmana1`](assets/minecraft/sounds/roaminlowonmana1.ogg?raw=true)                                         | `ambient`         |
| [`roaminlowonmana2`](assets/minecraft/sounds/roaminlowonmana2.ogg?raw=true)                                         | `ambient`         |
| [`roaminlowonmana3`](assets/minecraft/sounds/roaminlowonmana3.ogg?raw=true)                                         | `ambient`         |
| [`roaminoutofammo1`](assets/minecraft/sounds/roaminoutofammo1.ogg?raw=true)                                         | `ambient`         |
| [`roaminoutofammo2`](assets/minecraft/sounds/roaminoutofammo2.ogg?raw=true)                                         | `ambient`         |
| [`roaminoutofammo3`](assets/minecraft/sounds/roaminoutofammo3.ogg?raw=true)                                         | `ambient`         |
| [`roaminrecharged1`](assets/minecraft/sounds/roaminrecharged1.ogg?raw=true)                                         | `ambient`         |
| [`roaminrecharged2`](assets/minecraft/sounds/roaminrecharged2.ogg?raw=true)                                         | `ambient`         |
| [`roaminrecharged3`](assets/minecraft/sounds/roaminrecharged3.ogg?raw=true)                                         | `ambient`         |
| [`roaminrecharged4`](assets/minecraft/sounds/roaminrecharged4.ogg?raw=true)                                         | `ambient`         |
| [`goblinaction`](assets/minecraft/sounds/goblinaction1.ogg?raw=true)                                                | `ambient`         |
| [`goblinhurt`](assets/minecraft/sounds/goblinhurt1.ogg?raw=true)                                                    | `ambient`         |
| [`goblindie`](assets/minecraft/sounds/goblindie1.ogg?raw=true)                                                      | `ambient`         |
| [`goblinspawn`](assets/minecraft/sounds/goblinspawn1.ogg?raw=true)                                                  | `ambient`         |
| [`goblinkaboomready`](assets/minecraft/sounds/goblinkaboomready.ogg?raw=true)                                       | `ambient`         |
| [`goblinkaboomfire`](assets/minecraft/sounds/goblinkaboomfire.ogg?raw=true)                                         | `ambient`         |
| [`ogredie`](assets/minecraft/sounds/ogredie1.ogg?raw=true)                                                          | `ambient`         |
| [`ogreattack`](assets/minecraft/sounds/ogreattack1.ogg?raw=true)                                                    | `ambient`         |
| [`ogrehurt`](assets/minecraft/sounds/ogrehurt1.ogg?raw=true)                                                        | `ambient`         |
| [`ogrespawn`](assets/minecraft/sounds/ogrespawn1.ogg?raw=true)                                                      | `ambient`         |
| [`storejimmy`](assets/minecraft/sounds/storejimmy1.ogg?raw=true)                                                    | `ambient`         |
| [`monsterheroevent`](assets/minecraft/sounds/monsterheroevent.ogg?raw=true)                                         | `ambient`         |
| [`grand_paladin_authorization_required`](assets/minecraft/sounds/grand_paladin_authorization_required.ogg?raw=true) | `ambient`         |
| [`musical.levelup`](assets/minecraft/sounds/musical.levelup.ogg?raw=true)                                           | `ambient`         |
| [`rat.laugh`](assets/minecraft/sounds/rat.laugh.ogg?raw=true)                                                       | `ambient`         |
| [`bow.reload`](assets/minecraft/sounds/bow.reload.ogg?raw=true)                                                     | `ambient`         |
| [`sword.prepare`](assets/minecraft/sounds/sword.prepare.ogg?raw=true)                                               | `ambient`         |
| [`musical.oldgods`](assets/minecraft/sounds/musical.oldgods.ogg?raw=true)                                           | `ambient`         |
| [`deathsound`](assets/minecraft/sounds/deathsound.ogg?raw=true)                                                     | `player`          |
| [`sawmillaccident`](assets/minecraft/sounds/sawmillaccident.ogg?raw=true)                                           | `player`          |
| [`nisovin.tinderflameload`](assets/minecraft/sounds/nisovin.tinderflameload.ogg?raw=true)                           | `player`          |
| [`d20`](assets/minecraft/sounds/misc/d20.ogg?raw=true)                                                              | `player`          |
| [`pop`](assets/minecraft/sounds/misc/pop.ogg?raw=true)                                                              | `player`          |
| [`axe.chop`](assets/minecraft/sounds/axe/axe.chop1.ogg?raw=true)                                                    | `ambient`         |
| [`axe.timber`](assets/minecraft/sounds/axe/axe.timber1.ogg?raw=true)                                                | `ambient`         |
| [`pickaxe.mine`](assets/minecraft/sounds/pickaxe/pickaxe.mine1.ogg?raw=true)                                        | `ambient`         |
| [`pickaxe.break`](assets/minecraft/sounds/pickaxe/pickaxe.break1.ogg?raw=true)                                      | `ambient`         |
| [arcane.bigblast.ogg](assets/minecraft/sounds/spells/arcane.bigblast.ogg)                                           | `sound`           |
| [arcane.blast.ogg](assets/minecraft/sounds/spells/arcane.blast.ogg)                                                 | `sound`           |
| [arcane.blob.ogg](assets/minecraft/sounds/spells/arcane.blob.ogg)                                                   | `sound`           |
| [arcane.blobexplosion.ogg](assets/minecraft/sounds/spells/arcane.blobexplosion.ogg)                                 | `sound`           |
| [arcane.blobhit.ogg](assets/minecraft/sounds/spells/arcane.blobhit.ogg)                                             | `sound`           |
| [arcane.hit.ogg](assets/minecraft/sounds/spells/arcane.hit.ogg)                                                     | `sound`           |
| [arcane.mesmerize.ogg](assets/minecraft/sounds/spells/arcane.mesmerize.ogg)                                         | `sound`           |
| [arcane.mindcontrol.ogg](assets/minecraft/sounds/spells/arcane.mindcontrol.ogg)                                     | `sound`           |
| [arcane.powerdown.ogg](assets/minecraft/sounds/spells/arcane.powerdown.ogg)                                         | `sound`           |
| [arcane.powerloop.ogg](assets/minecraft/sounds/spells/arcane.powerloop.ogg)                                         | `sound`           |
| [arcane.resist.ogg](assets/minecraft/sounds/spells/arcane.resist.ogg)                                               | `sound`           |
| [arcane.shock.ogg](assets/minecraft/sounds/spells/arcane.shock.ogg)                                                 | `sound`           |
| [arcane.summon.ogg](assets/minecraft/sounds/spells/arcane.summon.ogg)                                               | `sound`           |
| [arcane.time.ogg](assets/minecraft/sounds/spells/arcane.time.ogg)                                                   | `sound`           |
| [arcane.tinkle.ogg](assets/minecraft/sounds/spells/arcane.tinkle.ogg)                                               | `sound`           |
| [arcane.wormhole.ogg](assets/minecraft/sounds/spells/arcane.wormhole.ogg)                                           | `sound`           |
| [cute.appear.ogg](assets/minecraft/sounds/spells/cute.appear.ogg)                                                   | `sound`           |
| [cute.cast.ogg](assets/minecraft/sounds/spells/cute.cast.ogg)                                                       | `sound`           |
| [cute.charge.ogg](assets/minecraft/sounds/spells/cute.charge.ogg)                                                   | `sound`           |
| [cute.explode.ogg](assets/minecraft/sounds/spells/cute.explode.ogg)                                                 | `sound`           |
| [cute.fall.ogg](assets/minecraft/sounds/spells/cute.fall.ogg)                                                       | `sound`           |
| [cute.get.ogg](assets/minecraft/sounds/spells/cute.get.ogg)                                                         | `sound`           |
| [cute.getbig.ogg](assets/minecraft/sounds/spells/cute.getbig.ogg)                                                   | `sound`           |
| [cute.getbiggest.ogg](assets/minecraft/sounds/spells/cute.getbiggest.ogg)                                           | `sound`           |
| [cute.hit.ogg](assets/minecraft/sounds/spells/cute.hit.ogg)                                                         | `sound`           |
| [cute.levelup.ogg](assets/minecraft/sounds/spells/cute.levelup.ogg)                                                 | `sound`           |
| [cute.reveal.ogg](assets/minecraft/sounds/spells/cute.reveal.ogg)                                                   | `sound`           |
| [cute.run.ogg](assets/minecraft/sounds/spells/cute.run.ogg)                                                         | `sound`           |
| [cute.summon.ogg](assets/minecraft/sounds/spells/cute.summon.ogg)                                                   | `sound`           |
| [cute.transformation.ogg](assets/minecraft/sounds/spells/cute.transformation.ogg)                                   | `sound`           |
| [cute.wink.ogg](assets/minecraft/sounds/spells/cute.wink.ogg)                                                       | `sound`           |
| [dark.appear.ogg](assets/minecraft/sounds/spells/dark.appear.ogg)                                                   | `sound`           |
| [dark.banshee1.ogg](assets/minecraft/sounds/spells/dark.banshee1.ogg)                                               | `sound`           |
| [dark.banshee2.ogg](assets/minecraft/sounds/spells/dark.banshee2.ogg)                                               | `sound`           |
| [dark.banshee3.ogg](assets/minecraft/sounds/spells/dark.banshee3.ogg)                                               | `sound`           |
| [dark.banshee4.ogg](assets/minecraft/sounds/spells/dark.banshee4.ogg)                                               | `sound`           |
| [dark.blink.ogg](assets/minecraft/sounds/spells/dark.blink.ogg)                                                     | `sound`           |
| [dark.cast.ogg](assets/minecraft/sounds/spells/dark.cast.ogg)                                                       | `sound`           |
| [dark.charge.ogg](assets/minecraft/sounds/spells/dark.charge.ogg)                                                   | `sound`           |
| [dark.curseexplode.ogg](assets/minecraft/sounds/spells/dark.curseexplode.ogg)                                       | `sound`           |
| [dark.demontalk1.ogg](assets/minecraft/sounds/spells/dark.demontalk1.ogg)                                           | `sound`           |
| [dark.demontalk2.ogg](assets/minecraft/sounds/spells/dark.demontalk2.ogg)                                           | `sound`           |
| [dark.demontalk3.ogg](assets/minecraft/sounds/spells/dark.demontalk3.ogg)                                           | `sound`           |
| [dark.demontalk4.ogg](assets/minecraft/sounds/spells/dark.demontalk4.ogg)                                           | `sound`           |
| [dark.detect.ogg](assets/minecraft/sounds/spells/dark.detect.ogg)                                                   | `sound`           |
| [dark.hit.ogg](assets/minecraft/sounds/spells/dark.hit.ogg)                                                         | `sound`           |
| [dark.mindcontrol.ogg](assets/minecraft/sounds/spells/dark.mindcontrol.ogg)                                         | `sound`           |
| [dark.misfire.ogg](assets/minecraft/sounds/spells/dark.misfire.ogg)                                                 | `sound`           |
| [dark.powerdown.ogg](assets/minecraft/sounds/spells/dark.powerdown.ogg)                                             | `sound`           |
| [dark.powersource.ogg](assets/minecraft/sounds/spells/dark.powersource.ogg)                                         | `sound`           |
| [dark.teleport.ogg](assets/minecraft/sounds/spells/dark.teleport.ogg)                                               | `sound`           |
| [dark.vanish.ogg](assets/minecraft/sounds/spells/dark.vanish.ogg)                                                   | `sound`           |
| [earth.blast.ogg](assets/minecraft/sounds/spells/earth.blast.ogg)                                                   | `sound`           |
| [earth.cast.ogg](assets/minecraft/sounds/spells/earth.cast.ogg)                                                     | `sound`           |
| [earth.cast2.ogg](assets/minecraft/sounds/spells/earth.cast2.ogg)                                                   | `sound`           |
| [earth.cast3.ogg](assets/minecraft/sounds/spells/earth.cast3.ogg)                                                   | `sound`           |
| [earth.gather.ogg](assets/minecraft/sounds/spells/earth.gather.ogg)                                                 | `sound`           |
| [earth.gather2.ogg](assets/minecraft/sounds/spells/earth.gather2.ogg)                                               | `sound`           |
| [earth.gather3.ogg](assets/minecraft/sounds/spells/earth.gather3.ogg)                                               | `sound`           |
| [earth.hit.ogg](assets/minecraft/sounds/spells/earth.hit.ogg)                                                       | `sound`           |
| [earth.hit2.ogg](assets/minecraft/sounds/spells/earth.hit2.ogg)                                                     | `sound`           |
| [earth.hit3.ogg](assets/minecraft/sounds/spells/earth.hit3.ogg)                                                     | `sound`           |
| [earth.metalland.ogg](assets/minecraft/sounds/spells/earth.metalland.ogg)                                           | `sound`           |
| [earth.powerdown.ogg](assets/minecraft/sounds/spells/earth.powerdown.ogg)                                           | `sound`           |
| [earth.prepare.ogg](assets/minecraft/sounds/spells/earth.prepare.ogg)                                               | `sound`           |
| [earth.shield.ogg](assets/minecraft/sounds/spells/earth.shield.ogg)                                                 | `sound`           |
| [fire.blast.ogg](assets/minecraft/sounds/spells/fire.blast.ogg)                                                     | `sound`           |
| [fire.blazeloop.ogg](assets/minecraft/sounds/spells/fire.blazeloop.ogg)                                             | `sound`           |
| [fire.bonloop.ogg](assets/minecraft/sounds/spells/fire.bonloop.ogg)                                                 | `sound`           |
| [fire.camploop.ogg](assets/minecraft/sounds/spells/fire.camploop.ogg)                                               | `sound`           |
| [fire.cast.ogg](assets/minecraft/sounds/spells/fire.cast.ogg)                                                       | `sound`           |
| [fire.cast2.ogg](assets/minecraft/sounds/spells/fire.cast2.ogg)                                                     | `sound`           |
| [fire.cast3.ogg](assets/minecraft/sounds/spells/fire.cast3.ogg)                                                     | `sound`           |
| [fire.fireball.ogg](assets/minecraft/sounds/spells/fire.fireball.ogg)                                               | `sound`           |
| [fire.gather.ogg](assets/minecraft/sounds/spells/fire.gather.ogg)                                                   | `sound`           |
| [fire.hit1.ogg](assets/minecraft/sounds/spells/fire.hit1.ogg)                                                       | `sound`           |
| [fire.hit2.ogg](assets/minecraft/sounds/spells/fire.hit2.ogg)                                                       | `sound`           |
| [fire.hit3.ogg](assets/minecraft/sounds/spells/fire.hit3.ogg)                                                       | `sound`           |
| [fire.hit4.ogg](assets/minecraft/sounds/spells/fire.hit4.ogg)                                                       | `sound`           |
| [fire.ignite.ogg](assets/minecraft/sounds/spells/fire.ignite.ogg)                                                   | `sound`           |
| [fire.release.ogg](assets/minecraft/sounds/spells/fire.release.ogg)                                                 | `sound`           |
| [fire.shield.ogg](assets/minecraft/sounds/spells/fire.shield.ogg)                                                   | `sound`           |
| [fire.summon.ogg](assets/minecraft/sounds/spells/fire.summon.ogg)                                                   | `sound`           |
| [fire.throw.ogg](assets/minecraft/sounds/spells/fire.throw.ogg)                                                     | `sound`           |
| [fire.throwfast.ogg](assets/minecraft/sounds/spells/fire.throwfast.ogg)                                             | `sound`           |
| [ice.blast.ogg](assets/minecraft/sounds/spells/ice.blast.ogg)                                                       | `sound`           |
| [ice.cast.ogg](assets/minecraft/sounds/spells/ice.cast.ogg)                                                         | `sound`           |
| [ice.gather.ogg](assets/minecraft/sounds/spells/ice.gather.ogg)                                                     | `sound`           |
| [ice.hit1.ogg](assets/minecraft/sounds/spells/ice.hit1.ogg)                                                         | `sound`           |
| [ice.hit2.ogg](assets/minecraft/sounds/spells/ice.hit2.ogg)                                                         | `sound`           |
| [ice.hit3.ogg](assets/minecraft/sounds/spells/ice.hit3.ogg)                                                         | `sound`           |
| [ice.hit4.ogg](assets/minecraft/sounds/spells/ice.hit4.ogg)                                                         | `sound`           |
| [light.bigblast.ogg](assets/minecraft/sounds/spells/light.bigblast.ogg)                                             | `sound`           |
| [light.buff.ogg](assets/minecraft/sounds/spells/light.buff.ogg)                                                     | `sound`           |
| [light.buff2.ogg](assets/minecraft/sounds/spells/light.buff2.ogg)                                                   | `sound`           |
| [light.charge.ogg](assets/minecraft/sounds/spells/light.charge.ogg)                                                 | `sound`           |
| [light.gather.ogg](assets/minecraft/sounds/spells/light.gather.ogg)                                                 | `sound`           |
| [light.heal.ogg](assets/minecraft/sounds/spells/light.heal.ogg)                                                     | `sound`           |
| [light.heal2.ogg](assets/minecraft/sounds/spells/light.heal2.ogg)                                                   | `sound`           |
| [light.powerdown.ogg](assets/minecraft/sounds/spells/light.powerdown.ogg)                                           | `sound`           |
| [light.powerup.ogg](assets/minecraft/sounds/spells/light.powerup.ogg)                                               | `sound`           |
| [light.shield.ogg](assets/minecraft/sounds/spells/light.shield.ogg)                                                 | `sound`           |
| [light.summon.ogg](assets/minecraft/sounds/spells/light.summon.ogg)                                                 | `sound`           |
| [light.teleport.ogg](assets/minecraft/sounds/spells/light.teleport.ogg)                                             | `sound`           |
| [poison.cast.ogg](assets/minecraft/sounds/spells/poison.cast.ogg)                                                   | `sound`           |
| [poison.hit1.ogg](assets/minecraft/sounds/spells/poison.hit1.ogg)                                                   | `sound`           |
| [poison.hit2.ogg](assets/minecraft/sounds/spells/poison.hit2.ogg)                                                   | `sound`           |
| [poison.hit3.ogg](assets/minecraft/sounds/spells/poison.hit3.ogg)                                                   | `sound`           |
| [poison.hit4.ogg](assets/minecraft/sounds/spells/poison.hit4.ogg)                                                   | `sound`           |
| [thunder.blast.ogg](assets/minecraft/sounds/spells/thunder.blast.ogg)                                               | `sound`           |
| [thunder.cast.ogg](assets/minecraft/sounds/spells/thunder.cast.ogg)                                                 | `sound`           |
| [thunder.cast2.ogg](assets/minecraft/sounds/spells/thunder.cast2.ogg)                                               | `sound`           |
| [thunder.gather.ogg](assets/minecraft/sounds/spells/thunder.gather.ogg)                                             | `sound`           |
| [thunder.gather2.ogg](assets/minecraft/sounds/spells/thunder.gather2.ogg)                                           | `sound`           |
| [thunder.hit.ogg](assets/minecraft/sounds/spells/thunder.hit.ogg)                                                   | `sound`           |
| [thunder.shield.ogg](assets/minecraft/sounds/spells/thunder.shield.ogg)                                             | `sound`           |
| [thunder.teleport.ogg](assets/minecraft/sounds/spells/thunder.teleport.ogg)                                         | `sound`           |
| [wind.bell.ogg](assets/minecraft/sounds/spells/wind.bell.ogg)                                                       | `sound`           |
| [wind.blast.ogg](assets/minecraft/sounds/spells/wind.blast.ogg)                                                     | `sound`           |
| [wind.blink.ogg](assets/minecraft/sounds/spells/wind.blink.ogg)                                                     | `sound`           |
| [wind.buff.ogg](assets/minecraft/sounds/spells/wind.buff.ogg)                                                       | `sound`           |
| [wind.cast.ogg](assets/minecraft/sounds/spells/wind.cast.ogg)                                                       | `sound`           |
| [wind.charge.ogg](assets/minecraft/sounds/spells/wind.charge.ogg)                                                   | `sound`           |
| [wind.echo.ogg](assets/minecraft/sounds/spells/wind.echo.ogg)                                                       | `sound`           |
| [wind.gather.ogg](assets/minecraft/sounds/spells/wind.gather.ogg)                                                   | `sound`           |
| [wind.gather2.ogg](assets/minecraft/sounds/spells/wind.gather2.ogg)                                                 | `sound`           |
| [wind.hit.ogg](assets/minecraft/sounds/spells/wind.hit.ogg)                                                         | `sound`           |
| [wind.hit2.ogg](assets/minecraft/sounds/spells/wind.hit2.ogg)                                                       | `sound`           |
| [wind.hit3.ogg](assets/minecraft/sounds/spells/wind.hit3.ogg)                                                       | `sound`           |
| [wind.implosion.ogg](assets/minecraft/sounds/spells/wind.implosion.ogg)                                             | `sound`           |
| [wind.prepare.ogg](assets/minecraft/sounds/spells/wind.prepare.ogg)                                                 | `sound`           |
| [wind.release.ogg](assets/minecraft/sounds/spells/wind.release.ogg)                                                 | `sound`           |
| [wind.teleport.ogg](assets/minecraft/sounds/spells/wind.teleport.ogg)                                               | `sound`           |
| [warpdrive.ogg](assets/minecraft/sounds/warpdrive.ogg)                                                              | `sound`           |
| [warpdriveend.ogg](assets/minecraft/sounds/warpdriveend.ogg)                                                        | `sound`           |
| [shipbeamup.ogg](assets/minecraft/sounds/shipbeamup.ogg)                                                            | `sound`           |
| [vampire.batform.off](assets/minecraft/sounds/vampire/vampire.batform.off.ogg)                                      | `sound`           |
| [vampire.batform.on](assets/minecraft/sounds/vampire/vampire.batform.on.ogg)                                        | `sound`           |
| [vampire.dagger](assets/minecraft/sounds/vampire/vampire.dagger1.ogg)                                               | `sound`           |
| [vampire.drain](assets/minecraft/sounds/vampire/vampire.drain.ogg)                                                  | `sound`           |
| [vampire.mesmerized](assets/minecraft/sounds/vampire/vampire.mesmerized.ogg)                                        | `sound`           |
| [vampire.shadowball.cast](assets/minecraft/sounds/vampire/vampire.shadowball.cast.ogg)                              | `sound`           |
| [vampire.shadowball.fire](assets/minecraft/sounds/vampire/vampire.shadowball.fire.ogg)                              | `sound`           |
| [vampire.shadowball.loop](assets/minecraft/sounds/vampire/vampire.shadowball.loop.ogg)                              | `sound`           |
| [vampire.stab](assets/minecraft/sounds/vampire/vampire.stab1.ogg)                                                   | `sound`           |
| [vampire.ticktock](assets/minecraft/sounds/vampire/vampire.ticktock.ogg)                                            | `sound`           |

## Models
The following items are used for different categories of custom models:
- Weapons/Tools: `music_disc_cat` - No crafting recipes, unplacable, unstackable
- Items: `rabbit_foot` - No crafting recipes, unplacable, stackable
- Hats/Helmets: `carved_pumpkin` - Wearable, no crafting recipes, but unfortunately placable and stackable ⚠ does not support transparency! ⚠
- Statues: also `carved_pumpkin` - Easy to place on armor stand, but current models have to be reworked for this
- Tools: nearest vanilla tool - depends on mining speed, (can be enchanted?)
- Special exceptions based on vanilla mechanics (Shields, Bows, Buffalo Horn, etc.)
- Custom GUIs: `jigsaw`

| name                          | item, custom model data | comments                          |
|-------------------------------|-------------------------|-----------------------------------|
| Excaliju                      | `music_disc_cat`, 1     | has animation?                    |
| Runeblade                     | `music_disc_cat`, 2     |                                   |
| Flamethrower                  | `music_disc_cat`, 3     |                                   |
| Elven Dagger                  | `music_disc_cat`, 4     |                                   |
| SOS                           | `music_disc_cat`, 5     |                                   |
| Warhammer                     | `music_disc_cat`, 6     |                                   |
| Hammer                        | `music_disc_cat`, 7     |                                   |
| Malice                        | `music_disc_cat`, 8     |                                   |
| Gravedigger                   | `music_disc_cat`, 9     |                                   |
| Flame Fist                    | `music_disc_cat`, 10    |                                   |
| Flame Bow                     | `music_disc_cat`, 11    |                                   |
| Emerald Bow                   | `music_disc_cat`, 12    |                                   |
| Wand of Fire                  | `music_disc_cat`, 13    |                                   |
| Tombmaker                     | `music_disc_cat`, 14    |                                   |
| Staff of Defile               | `music_disc_cat`, 15    |                                   |
| Wand of Limited Probabilities | `music_disc_cat`, 16    |                                   |
| Tinder Flame                  | `music_disc_cat`, 17    |                                   |
| Dwarven Crossbow              | `music_disc_cat`, 18    | needs to be converted to 3d model |
| Wiggly Wrench                 | `music_disc_cat`, 19    |                                   |
| Quiver                        | `music_disc_cat`, 20    |                                   |
| Spellbook                     | `music_disc_cat`, 21    |                                   |
| Foamer                        | `music_disc_cat`, 22    |                                   |
| Flintlock                     | `music_disc_cat`, 23    |                                   |
| Blunderbuss                   | `music_disc_cat`, 24    |                                   |
| Dirt Hose                     | `music_disc_cat`, 25    |                                   |
| Oxygen Tanks                  | `music_disc_cat`, 26    |                                   |
| Farmer Basket                 | `music_disc_cat`, 27    |                                   |
| Plant in a Bottle             | `music_disc_cat`, 28    |                                   |
| Quiver                        | `music_disc_cat`, 29    |                                   |
| Urn                           | `music_disc_cat`, 30    |                                   |
| Witches Cauldron              | `music_disc_cat`, 31    |                                   |
| Abyss Wings                   | `music_disc_cat`, 32    |                                   |
| D20                           | `rabbit_foot`, 1        |                                   |
| Scroll                        | `rabbit_foot`, 2        |                                   |
| Mortar                        | `rabbit_foot`, 3        |                                   |
| Wizard Mortar                 | `rabbit_foot`, 4        |                                   |
| Dwarven Log                   | `rabbit_foot`, 5        |                                   |
| Dwarven Planks                | `rabbit_foot`, 6        |                                   |
| Invisible                     | `rabbit_foot`, 7        |                                   |
| Buffalo Horn                  | `goat_horn`, 1          |                                   |
| Lumberjack Axe                | `stone_axe`, 1          |                                   |
| Dwarven Pickaxe               | `iron_pickaxe`, 1       |                                   |
| Dwarven Shovel                | `iron_shovel`, 1        |                                   |
| Abyss Shovel                  | `iron_shovel`, 2        |                                   |
| Abyss Sword                   | `iron_sword`, 1         |                                   |
| Dwarven Axe                   | `iron_axe`, 1           |                                   |
| Ancient Pickaxe               | `diamond_pickaxe`, 1    |                                   |
| Dwarven Chestplate            | `diamond_chestplate`, 1 |                                   |
| Buckler                       | `shield`, 1             |                                   |
| Heater                        | `shield`, 2             |                                   |
| Targe                         | `shield`, 3             |                                   |
| Rapier                        | `shield`, 4             |                                   |
| Abyss Bow                     | `bow`, 1                |                                   |
| Beard                         | `carved_pumpkin`, 1     |                                   |
| Dwarven Beard                 | `carved_pumpkin`, 2     |                                   |
| Roamin Helmet                 | `carved_pumpkin`, 3     |                                   |
| Knight Helm                   | `carved_pumpkin`, 4     |                                   |
| Wizard Hat                    | `carved_pumpkin`, 5     |                                   |
| Imperfect Crown               | `carved_pumpkin`, 6     |                                   |
| Tiara                         | `carved_pumpkin`, 7     |                                   |
| Shell Wall                    | `carved_pumpkin`, 8     |                                   |
| Fallen Valk                   | `carved_pumpkin`, 9     |                                   |
| Pharaoh                       | `carved_pumpkin`, 10    |                                   |
| The Buccaneer                 | `carved_pumpkin`, 11    |                                   |
| Shaman Mask                   | `carved_pumpkin`, 12    |                                   |
| The Wolf Hunter               | `carved_pumpkin`, 13    |                                   |
| Dragon's Breath               | `carved_pumpkin`, 14    | animated                          |
| Bull Horn                     | `carved_pumpkin`, 15    |                                   |
| Wowzers                       | `carved_pumpkin`, 16    |                                   |
| Tophat                        | `carved_pumpkin`, 17    |                                   |
| Gnomish Googles               | `carved_pumpkin`, 18    |                                   |
| Dragon Warrior                | `carved_pumpkin`, 19    |                                   |
| Nismas Hat                    | `carved_pumpkin`, 20    |                                   |
| Chameleon                     | `carved_pumpkin`, 21    | animated                          |
| Rainbow Kitty                 | `carved_pumpkin`, 22    | animated                          |
| Mama                          | `carved_pumpkin`, 23    |                                   |
| Mama 2                        | `carved_pumpkin`, 24    | blue                              |
| Mama 3                        | `carved_pumpkin`, 25    | purple                            |
| Mama 4                        | `carved_pumpkin`, 26    | orange                            |
| Mama 5                        | `carved_pumpkin`, 27    | green                             |
| Jimmy The Rat                 | `carved_pumpkin`, 28    |                                   |
| Headbox                       | `carved_pumpkin`, 29    |                                   |
| Knight Helmet Red             | `carved_pumpkin`, 30    |                                   |
| Knight Helmet Green           | `carved_pumpkin`, 31    |                                   |
| Zombie Statue                 | `carved_pumpkin`, 1001  | Walking                           |
| Zombie Statue                 | `carved_pumpkin`, 1002  | Standing                          |
| Zombie Statue                 | `carved_pumpkin`, 1003  | Crawling                          |
| Zombie Statue                 | `carved_pumpkin`, 1004  | Sneaking                          |
| Bruce Statue                  | `carved_pumpkin`, 1005  | Heroic                            |
| Tinder Flame (3D model)       | `spyglass`, 1           |                                   |
| Ale                           | `honey_bottle`, 1       |                                   |
| Skill Tree GUI                | `jigsaw`, 1             | row 2, col 1 of 3-row inventory   |
| Class Selection GUI           | `jigsaw`, 2             | row 2, col 1 of 3-row inventory   |
| Icon: Baker Class             | `jigsaw`, 3             | icon, 1x1                         |
| Icon: Berserker Class         | `jigsaw`, 4             | icon, 1x1                         |
| Icon: Blacksmith Class        | `jigsaw`, 5             | icon, 1x1                         |
| Icon: Builder Class           | `jigsaw`, 6             | icon, 1x1                         |
| Icon: High Paladin Class      | `jigsaw`, 7             | icon, 1x1                         |
| Icon: Paladin Class           | `jigsaw`, 8             | icon, 1x1                         |
| Icon: Ranger Class            | `jigsaw`, 9             | icon, 1x1                         |
| Icon: Warriror Class          | `jigsaw`, 10            | icon, 1x1                         |

## Textures
In addition to adding custom textures for the models, the following textures of existing items have been changed:
- `textures/item/gold_nugget.png`
- `textures/item/goat_horn.png`

The following textures of mobs have been changed:
- Gobo - `textures/entity/creeper/creeper.png`
- Vlaurunga - `textures/entity/enderdragon/dragon.png`
- Vlaurunga - `textures/entity/enderdragon/dragon_eyes.png`
- Sandworm - `textures/entity/ghast/ghast.png`
- Sandworm - `textures/entity/ghast/ghast_shooting.png`
- Lava Spider - `textures/entity/spider/spider.png`
- Poison Spider - `textures/entity/spider/cave_spider.png`
- Demon Warden - `textures/entity/warden/warden.png`
- Demon Warden - `textures/entity/warden/warden_bioluminescent_layer.png`
- Demon Warden - `textures/entity/warden/warden_heart.png`
- Demon Warden - `textures/entity/warden/warden_pulsating_spots_1.png`
- Demon Warden - `textures/entity/warden/warden_pulsating_spots_2.png`
- Wolf - `textures/entity/wolf/wolf.png`
- Wolf - `textures/entity/wolf/wolf_angry.png`
- Nisovin - `textures/entity/zombie/husk.png`
- Pause Blaze - `textures/entity/blaze.png`
- Swammy - `textures/entity/endermite.png`
- Bone Phantom - `textures/entity/phantom.png`
- Phantom Eyes - `textures.entity/phantom_eyes.png`
- Allay - `textures/entity/allay.png`
- Goat - `textures/entity/goat/goat.png`
- Ravager - `textures/entity/illager/ravager.png`
- Iron Golem - `textures/entity/iron_golem/iron_golem.png`
- Iron Golem Crackiness High - `textures/entity/iron_golem/iron_golem_crackiness_high.png`
- Iron Golem Crackiness Low - `textures/entity/iron_golem/iron_golem_crackiness_low.png`
- Iron Golem Crackiness Medium - `textures/entity/iron_golem/iron_golem_crackiness_medium.png`
- Brown Panda - `textures/entity/panda/brown_panda.png`
- Maid Panda - `textures/entity/panda/playful_panda.png`
- Weak Panda - `textures/entity/panda/weak_panda.png`
- Worried Panda - `textures/entity/panda/worried_panda.png`


The following armor textures have been changed:
- `textures/models/armor/chainmail_layer_1.png`
- `textures/models/armor/chainmail_layer_2.png`
- `textures/models/armor/diamond_layer_1.png`
- `textures/models/armor/diamond_layer_2.png`
- `textures/models/armor/iron_layer_1.png`
- `textures/models/armor/iron_layer_2.png`

The following blocks have been changed:
- Sword Pickup - `textures/blocks/ladder.png`
- Bow Pickup - `textures/blocks/detector_rail.png`
- Axe Pickup - `textures/blocks/rail.png`
- Pickaxe Pickup - `textures/blocks/activator_rail.png`
- Juice Pickup - `textures/blocks/redstone_torch.png`
- Juice Pickup - `textures/blocks/redstone_torch_off.png`
- Sawmill - `textures/blocks/iron_bars.png`
- Conveyor Belt - `textures/blocks/piston_side.png`
- Conveyor Belt - `textures/blocks/piston_top_normal.png`
- Conveyor Belt - `textures/blocks/piston_top_sticky.png`
- Oil - `textures/blocks/sponge.png`
- Blue Bricks - `textures/blocks/lapis_ore.png`
- Darker Stone - `textures/blocks/bedrock.png`
- Shrine - `textures/blocks/end_portal_frame_side.png`
- Shrine - `textures/blocks/end_portal_frame_top.png`
- Goblin Bomb - `textures/blocks/end_stone.png`
- Gobo TNT - `textures/blocks/tnt_bottom.png`
- Gobo TNT - `textures/blocks/tnt_side.png`
- Gobo TNT - `textures/blocks/tnt_top.png`
- Smooth Gold - `textures/blocks/gold_block.png`
- Armor Crafting Mk. 1 - `textures/blocks/orange_wool.png`
- Armor Crafting Mk. 2 - `textures/blocks/yellow_wool.png`
- Armor Crafting Mk. 3 - `textures/blocks/magenta_wool.png`
- Spider Poison - `textures/blocks/lime_wool.png`
- Demon Catalyst - `textures/blocks/skulk_catalyst_bottom.png`
- Demon Catalyst - `textures/blocks/skulk_catalyst_side.png`
- Demon Catalyst - `textures/blocks/skulk_catalyst_side_bloom.png`
- Demon Catalyst - `textures/blocks/skulk_catalyst_top.png`
- Demon Catalyst - `textures/blocks/skulk_catalyst_top_bloom.png`
- Demon Sensor - `textures/blocks/skulk_sensor_bottom.png`
- Demon Sensor - `textures/blocks/skulk_sensor_side.png`
- Demon Sensor - `textures/blocks/skulk_sensor_tendril_active.png`
- Demon Sensor - `textures/blocks/skulk_sensor_tendril_inactive.png`
- Demon Sensor - `textures/blocks/skulk_sensor_top.png`
- Demon Shrieker - `textures/blocks/skulk_shrieker_bottom.png`
- Demon Shrieker - `textures/blocks/sculk_shrieker_can_summon_inner_top.png`
- Demon Shrieker - `textures/blocks/sculk_shrieker_inner_top.png`
- Demon Shrieker - `textures/blocks/skulk_shrieker_side.png`
- Demon Shrieker - `textures/blocks/skulk_shrieker_top.png`
- Demon Vein - `textures/blocks/skulk_vein.png`
- Demon Block - `textures/blocks/skulk.png`
- Demon Campfire - `textures/blocks/soul_campfire_fire.png`
- Demon Campfire - `textures/blocks/soul_campfire_log_lit.png`
- Demon Fire - `textures/blocks/soul_fire_0.png`
- Demon Fire - `textures/blocks/soul_fire_1.png`
- Demon Lantern - `textures/blocks/soul_lantern.png`
- Blood Splatter Dot - `textures/blocks/redstone_dust_dot.png`
- Blood Splatter Line1 - `textures/blocks/redstone_dust_line0.png`
- Blood Splatter Line2 - `textures/blocks/redstone_dust_line1.png`
- Redstone Block (animated) - `textures/blocks/redstone_dust_line1.png`

The following GUI textures have been added/changed:
- `textures/gui/widgets.png` - Dark toolbar by VanillaTweaks
- `textures/gui/containers/inventory.png` - Dark gui by VanillaTweaks, modified
- `textures/gui/containers/generic_54.png` - Dark gui by VanillaTweaks, modified

# TODO:
- Move custom resources to dvz namespace
  - Add warden sounds to sounds.json
- Rename sounds group related sounds together
- Update icons.png
  - attack cooldown indicators
- Fix Excaliju animation
- Fix Custom Bow pulling
- retexture dragon fireball
- replace custom block textures in the model files rather than overwriting vanilla textures (see pumpkin)
- Modify Zombified Piglin texture similar to the old Zombie Pigman