# DvZ
Resource pack for DvZ 1.19.2

## Language Edits
The following Changes have been made to the main English language files (`en_AU`, `en_CA`, `en_GB`, `en_US`):
| key                     | original (`en_US`)  | custom                |
|-------------------------|---------------------|-----------------------|
| `soundCategory.ambient` | Ambient/Environment | Hero Warnings/Events* |
| `soundCategory.block`   | Blocks              | Blocks                |
| `soundCategory.hostile` | Hostile Creatures   | Mobs*                 |
| `soundCategory.master`  | Master Volume       | Master Volume         |
| `soundCategory.music`   | Music               | Minecraft Music*      |
| `soundCategory.neutral` | Friendly Creatures  | DvZ Music*            |
| `soundCategory.player`  | Players             | Jimmies*              |
| `soundCategory.record`  | Jukebox/Note Blocks | Heroes Messages*      |
| `soundCategory.voice`   | Voice/Speech        | Voice/Speech          |
| `soundCategory.weather` | Weather             | Tools/Crafting*       |
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
| [`nisovin.tinderflameload`](assets/minecraft/sounds/nisovin.tinderflameload.ogg?raw=true)                           | `weather`         |