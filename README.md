# DvZ
Resource pack for DvZ 1.19.2

## Content

### Language Edits
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

### Sounds
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

The following custom sounds have been added:
| key                                    | example                                                                                         | intended category |
|----------------------------------------|-------------------------------------------------------------------------------------------------|-------------------|
| `activatebow`                          | <audio src="assets/minecraft/sounds/activatebow.ogg" controls></audio>                          | `weather`         |
| `activateshield`                       | <audio src="assets/minecraft/sounds/activateshield.ogg" controls></audio>                       | `weather`         |
| `activatesword`                        | <audio src="assets/minecraft/sounds/activatesword.ogg" controls></audio>                        | `weather`         |
| `toolaxehit`                           | <audio src="assets/minecraft/sounds/toolaxehit1.ogg" controls></audio>                          | `weather`         |
| `toolwoodchop`                         | <audio src="assets/minecraft/sounds/toolwoodchop1.ogg" controls></audio>                        | `weather`         |
| `wpnmonstersmash`                      | <audio src="assets/minecraft/sounds/wpnmonstersmash1.ogg" controls></audio>                     | `weather`         |
| `wpnmonstersmashbig`                   | <audio src="assets/minecraft/sounds/wpnmonstersmashbig1.ogg" controls></audio>                  | `weather`         |
| `wpnwarhammer`                         | <audio src="assets/minecraft/sounds/wpnwarhammer1.ogg" controls></audio>                        | `weather`         |
| `wpncrossbow`                          | <audio src="assets/minecraft/sounds/wpncrossbow1.ogg" controls></audio>                         | `weather`         |
| `emeraldbowfire`                       | <audio src="assets/minecraft/sounds/emeraldbowfire1.ogg" controls></audio>                      | `weather`         |
| `emeraldbowdraw`                       | <audio src="assets/minecraft/sounds/emeraldbowdraw.ogg" controls></audio>                       | `weather`         |
| `hatgoggles`                           | <audio src="assets/minecraft/sounds/hatgoggles1.ogg" controls></audio>                          | `sound`           |
| `hatdragonwarrior`                     | <audio src="assets/minecraft/sounds/hatdragonwarrior.ogg" controls></audio>                     | `sound`           |
| `hatdragonsbreath`                     | <audio src="assets/minecraft/sounds/hatdragonsbreath.ogg" controls></audio>                     | `sound`           |
| `hatpharaoh`                           | <audio src="assets/minecraft/sounds/hatpharaoh.ogg" controls></audio>                           | `sound`           |
| `hatsunglasses`                        | <audio src="assets/minecraft/sounds/hatsunglasses.ogg" controls></audio>                        | `sound`           |
| `hatwolfhunter`                        | <audio src="assets/minecraft/sounds/hatwolfhunter.ogg" controls></audio>                        | `sound`           |
| `general.offcooldown`                  | <audio src="assets/minecraft/sounds/general.offcooldown.ogg" controls></audio>                  | `sound`           |
| `doomeventbarnyard`                    | <audio src="assets/minecraft/sounds/doomeventbarnyard.ogg" controls></audio>                    | `ambient`         |
| `doomeventbopen`                       | <audio src="assets/minecraft/sounds/doomeventbopen.ogg" controls></audio>                       | `ambient`         |
| `doomeventkrungor`                     | <audio src="assets/minecraft/sounds/doomeventkrungor.ogg" controls></audio>                     | `ambient`         |
| `doomevent1`                           | <audio src="assets/minecraft/sounds/doomevent1.ogg" controls></audio>                           | `ambient`         |
| `doomevent2`                           | <audio src="assets/minecraft/sounds/doomevent2.ogg" controls></audio>                           | `ambient`         |
| `doomevent3`                           | <audio src="assets/minecraft/sounds/doomevent3.ogg" controls></audio>                           | `ambient`         |
| `doomevent4`                           | <audio src="assets/minecraft/sounds/doomevent4.ogg" controls></audio>                           | `ambient`         |
| `doomevent5`                           | <audio src="assets/minecraft/sounds/doomevent5.ogg" controls></audio>                           | `ambient`         |
| `wpnwarpweaver`                        | <audio src="assets/minecraft/sounds/wpnwarpweaver.ogg" controls></audio>                        | `weather`         |
| `wpnplunder`                           | <audio src="assets/minecraft/sounds/wpnplunder.ogg" controls></audio>                           | `weather`         |
| `wind`                                 | <audio src="assets/minecraft/sounds/wind.ogg" controls></audio>                                 | `sounds`          |
| `wpnsos`                               | <audio src="assets/minecraft/sounds/wpnsos.ogg" controls></audio>                               | `ambient`         |
| `magiccoil`                            | <audio src="assets/minecraft/sounds/magiccoil.ogg" controls></audio>                            | `ambient`         |
| `wpnbuffalohorn`                       | <audio src="assets/minecraft/sounds/wpnbuffalohorn.ogg" controls></audio>                       | `ambient`         |
| `wpnproc`                              | <audio src="assets/minecraft/sounds/wpnproc.ogg" controls></audio>                              | `ambient`         |
| `general.hitding`                      | <audio src="assets/minecraft/sounds/general.hitding.ogg" controls></audio>                      | `sounds`          |
| `warhammercharge`                      | <audio src="assets/minecraft/sounds/warhammercharge.ogg" controls></audio>                      | `ambient`         |
| `warhammerrankup`                      | <audio src="assets/minecraft/sounds/warhammerrankup.ogg" controls></audio>                      | `ambient`         |
| `runebladerunedash`                    | <audio src="assets/minecraft/sounds/runebladerunedash.ogg" controls></audio>                    | `ambient`         |
| `wpnenchantedlamp`                     | <audio src="assets/minecraft/sounds/wpnenchantedlamp.ogg" controls></audio>                     | `weather`         |
| `coin`                                 | <audio src="assets/minecraft/sounds/misc/coin.ogg" controls></audio>                            | `player`          |
| `coinflip`                             | <audio src="assets/minecraft/sounds/misc/coinflip.ogg" controls></audio>                        | `player`          |
| `brucecasual1`                         | <audio src="assets/minecraft/sounds/brucecasual1.ogg" controls></audio>                         | `record`          |
| `brucecombatgeneral1`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral1.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral2`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral2.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral3`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral3.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral4`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral4.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral5`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral5.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral6`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral6.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral7`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral7.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral8`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral8.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral9`                  | <audio src="assets/minecraft/sounds/brucecombatgeneral9.ogg" controls></audio>                  | `record`          |
| `brucecombatgeneral10`                 | <audio src="assets/minecraft/sounds/brucecombatgeneral10.ogg" controls></audio>                 | `record`          |
| `brucecombatgeneral11`                 | <audio src="assets/minecraft/sounds/brucecombatgeneral11.ogg" controls></audio>                 | `record`          |
| `brucecombatgeneral12`                 | <audio src="assets/minecraft/sounds/brucecombatgeneral12.ogg" controls></audio>                 | `record`          |
| `brucecombatgeneral13`                 | <audio src="assets/minecraft/sounds/brucecombatgeneral13.ogg" controls></audio>                 | `record`          |
| `brucecombatindoors1`                  | <audio src="assets/minecraft/sounds/brucecombatindoors1.ogg" controls></audio>                  | `record`          |
| `brucecombatindoors2`                  | <audio src="assets/minecraft/sounds/brucecombatindoors2.ogg" controls></audio>                  | `record`          |
| `brucecombatindoors3`                  | <audio src="assets/minecraft/sounds/brucecombatindoors3.ogg" controls></audio>                  | `record`          |
| `brucecombatindoors4`                  | <audio src="assets/minecraft/sounds/brucecombatindoors4.ogg" controls></audio>                  | `record`          |
| `brucecombatoutdoors1`                 | <audio src="assets/minecraft/sounds/brucecombatoutdoors1.ogg" controls></audio>                 | `record`          |
| `brucecombatoutdoors2`                 | <audio src="assets/minecraft/sounds/brucecombatoutdoors2.ogg" controls></audio>                 | `record`          |
| `brucecombatoutdoors3`                 | <audio src="assets/minecraft/sounds/brucecombatoutdoors3.ogg" controls></audio>                 | `record`          |
| `brucecombatoutdoors4`                 | <audio src="assets/minecraft/sounds/brucecombatoutdoors4.ogg" controls></audio>                 | `record`          |
| `brucecombatoutdoors5`                 | <audio src="assets/minecraft/sounds/brucecombatoutdoors5.ogg" controls></audio>                 | `record`          |
| `bruceexplosionnearby1`                | <audio src="assets/minecraft/sounds/bruceexplosionnearby1.ogg" controls></audio>                | `record`          |
| `bruceexplosionnearby2`                | <audio src="assets/minecraft/sounds/bruceexplosionnearby2.ogg" controls></audio>                | `record`          |
| `brucedeath`                           | <audio src="assets/minecraft/sounds/brucedeath.ogg" controls></audio>                           | `ambient`         |
| `brucediggingzombiewarning`            | <audio src="assets/minecraft/sounds/brucediggingzombiewarning.ogg" controls></audio>            | `ambient`         |
| `brucegolemwarning`                    | <audio src="assets/minecraft/sounds/brucegolemwarning1.ogg" controls></audio>                   | `ambient`         |
| `bruceintro`                           | <audio src="assets/minecraft/sounds/bruceintro.ogg" controls></audio>                           | `ambient`         |
| `brucelowonmana1`                      | <audio src="assets/minecraft/sounds/brucelowonmana1.ogg" controls></audio>                      | `record`          |
| `brucelowonmana2`                      | <audio src="assets/minecraft/sounds/brucelowonmana2.ogg" controls></audio>                      | `record`          |
| `brucelowonmana3`                      | <audio src="assets/minecraft/sounds/brucelowonmana3.ogg" controls></audio>                      | `record`          |
| `bruceproc1`                           | <audio src="assets/minecraft/sounds/bruceproc1.ogg" controls></audio>                           | `record`          |
| `bruceproc2`                           | <audio src="assets/minecraft/sounds/bruceproc2.ogg" controls></audio>                           | `record`          |
| `bruceproc3`                           | <audio src="assets/minecraft/sounds/bruceproc3.ogg" controls></audio>                           | `record`          |
| `bruceproc`                            | <audio src="assets/minecraft/sounds/bruceproc1.ogg" controls></audio>                           | `ambient`         |
| `bruceratswarning`                     | <audio src="assets/minecraft/sounds/bruceratswarning1.ogg" controls></audio>                    | `ambient`         |
| `bruceshrinedestroyed1`                | <audio src="assets/minecraft/sounds/bruceshrinedestroyed1.ogg" controls></audio>                | `ambient`         |
| `bruceshrinedestroyed2`                | <audio src="assets/minecraft/sounds/bruceshrinedestroyed2.ogg" controls></audio>                | `ambient`         |
| `bruceshrinedestroyed3`                | <audio src="assets/minecraft/sounds/bruceshrinedestroyed3.ogg" controls></audio>                | `ambient`         |
| `brucespideringswarning`               | <audio src="assets/minecraft/sounds/brucespideringswarning1.ogg" controls></audio>              | `ambient`         |
| `brucevenomburnerswarning`             | <audio src="assets/minecraft/sounds/brucevenomburnerswarning1.ogg" controls></audio>            | `ambient`         |
| `brucewolveswarning`                   | <audio src="assets/minecraft/sounds/brucewolveswarning1.ogg" controls></audio>                  | `ambient`         |
| `brucemonstersreleased`                | <audio src="assets/minecraft/sounds/brucemonstersreleased.ogg" controls></audio>                | `ambient`         |
| `brucenoprocwarning`                   | <audio src="assets/minecraft/sounds/brucenoprocwarning1.ogg" controls></audio>                  | `ambient`         |
| `brucenomanawarning`                   | <audio src="assets/minecraft/sounds/brucenomanawarning1.ogg" controls></audio>                  | `ambient`         |
| `brucenorepairwarning`                 | <audio src="assets/minecraft/sounds/brucenorepairwarning1.ogg" controls></audio>                | `ambient`         |
| `maliceintro`                          | <audio src="assets/minecraft/sounds/maliceintro.ogg" controls></audio>                          | `ambient`         |
| `malicegeneral`                        | <audio src="assets/minecraft/sounds/malicegeneral1.ogg" controls></audio>                       | `record`          |
| `maliceuse`                            | <audio src="assets/minecraft/sounds/maliceuse1.ogg" controls></audio>                           | `record`          |
| `daragorattack`                        | <audio src="assets/minecraft/sounds/daragorattack1.ogg" controls></audio>                       | `ambient`         |
| `daragordeath`                         | <audio src="assets/minecraft/sounds/daragordeath.ogg" controls></audio>                         | `ambient`         |
| `daragorspawn`                         | <audio src="assets/minecraft/sounds/daragorspawn.ogg" controls></audio>                         | `ambient`         |
| `daragortaunt`                         | <audio src="assets/minecraft/sounds/daragortaunt1.ogg" controls></audio>                        | `ambient`         |
| `daragorworldcracker`                  | <audio src="assets/minecraft/sounds/daragorworldcracker1.ogg" controls></audio>                 | `ambient`         |
| `dvzlore1`                             | <audio src="assets/minecraft/sounds/dvzlore1.ogg" controls></audio>                             | `neutral`         |
| `dvzlore2`                             | <audio src="assets/minecraft/sounds/dvzlore2.ogg" controls></audio>                             | `neutral`         |
| `dvzlore3`                             | <audio src="assets/minecraft/sounds/dvzlore3.ogg" controls></audio>                             | `neutral`         |
| `dvzlore4`                             | <audio src="assets/minecraft/sounds/dvzlore4.ogg" controls></audio>                             | `neutral`         |
| `dvzlore5`                             | <audio src="assets/minecraft/sounds/dvzlore5.ogg" controls></audio>                             | `neutral`         |
| `dvzlore6`                             | <audio src="assets/minecraft/sounds/dvzlore6.ogg" controls></audio>                             | `neutral`         |
| `dvzlore7`                             | <audio src="assets/minecraft/sounds/dvzlore7.ogg" controls></audio>                             | `neutral`         |
| `dvzlore8`                             | <audio src="assets/minecraft/sounds/dvzlore8.ogg" controls></audio>                             | `neutral`         |
| `dvzlore9`                             | <audio src="assets/minecraft/sounds/dvzlore9.ogg" controls></audio>                             | `neutral`         |
| `dvzlore10`                            | <audio src="assets/minecraft/sounds/dvzlore10.ogg" controls></audio>                            | `neutral`         |
| `dvzlore11`                            | <audio src="assets/minecraft/sounds/dvzlore11.ogg" controls></audio>                            | `neutral`         |
| `dvzlore12`                            | <audio src="assets/minecraft/sounds/dvzlore12.ogg" controls></audio>                            | `neutral`         |
| `dvzlore13`                            | <audio src="assets/minecraft/sounds/dvzlore13.ogg" controls></audio>                            | `neutral`         |
| `dvzlore14`                            | <audio src="assets/minecraft/sounds/dvzlore14.ogg" controls></audio>                            | `neutral`         |
| `dvzlore15`                            | <audio src="assets/minecraft/sounds/dvzlore15.ogg" controls></audio>                            | `neutral`         |
| `dvzlore16`                            | <audio src="assets/minecraft/sounds/dvzlore16.ogg" controls></audio>                            | `neutral`         |
| `dvzlore17`                            | <audio src="assets/minecraft/sounds/dvzlore17.ogg" controls></audio>                            | `neutral`         |
| `dvzlore18`                            | <audio src="assets/minecraft/sounds/dvzlore18.ogg" controls></audio>                            | `neutral`         |
| `dvzlore19`                            | <audio src="assets/minecraft/sounds/dvzlore19.ogg" controls></audio>                            | `neutral`         |
| `dvzlore20`                            | <audio src="assets/minecraft/sounds/dvzlore20.ogg" controls></audio>                            | `neutral`         |
| `dvzlore21`                            | <audio src="assets/minecraft/sounds/dvzlore21.ogg" controls></audio>                            | `neutral`         |
| `dvzlore22`                            | <audio src="assets/minecraft/sounds/dvzlore22.ogg" controls></audio>                            | `neutral`         |
| `dvzlore23`                            | <audio src="assets/minecraft/sounds/dvzlore23.ogg" controls></audio>                            | `neutral`         |
| `dvzlore24`                            | <audio src="assets/minecraft/sounds/dvzlore24.ogg" controls></audio>                            | `neutral`         |
| `dvzlore25`                            | <audio src="assets/minecraft/sounds/dvzlore25.ogg" controls></audio>                            | `neutral`         |
| `dvzlore26`                            | <audio src="assets/minecraft/sounds/dvzlore26.ogg" controls></audio>                            | `neutral`         |
| `dvzlore27`                            | <audio src="assets/minecraft/sounds/dvzlore27.ogg" controls></audio>                            | `neutral`         |
| `dvzlore28`                            | <audio src="assets/minecraft/sounds/dvzlore28.ogg" controls></audio>                            | `neutral`         |
| `dvzlore29`                            | <audio src="assets/minecraft/sounds/dvzlore29.ogg" controls></audio>                            | `neutral`         |
| `dvzlore30`                            | <audio src="assets/minecraft/sounds/dvzlore30.ogg" controls></audio>                            | `neutral`         |
| `dvzlore31`                            | <audio src="assets/minecraft/sounds/dvzlore31.ogg" controls></audio>                            | `neutral`         |
| `dvzlore32`                            | <audio src="assets/minecraft/sounds/dvzlore32.ogg" controls></audio>                            | `neutral`         |
| `dvzlore33`                            | <audio src="assets/minecraft/sounds/dvzlore33.ogg" controls></audio>                            | `neutral`         |
| `dvzlore34`                            | <audio src="assets/minecraft/sounds/dvzlore34.ogg" controls></audio>                            | `neutral`         |
| `dvzlore35`                            | <audio src="assets/minecraft/sounds/dvzlore35.ogg" controls></audio>                            | `neutral`         |
| `dvzlore36`                            | <audio src="assets/minecraft/sounds/dvzlore36.ogg" controls></audio>                            | `neutral`         |
| `dvzlore37`                            | <audio src="assets/minecraft/sounds/dvzlore37.ogg" controls></audio>                            | `neutral`         |
| `dvzlore38`                            | <audio src="assets/minecraft/sounds/dvzlore38.ogg" controls></audio>                            | `neutral`         |
| `dvzlore39`                            | <audio src="assets/minecraft/sounds/dvzlore39.ogg" controls></audio>                            | `neutral`         |
| `dvzlore40`                            | <audio src="assets/minecraft/sounds/dvzlore40.ogg" controls></audio>                            | `neutral`         |
| `dvzlore41`                            | <audio src="assets/minecraft/sounds/dvzlore41.ogg" controls></audio>                            | `neutral`         |
| `dvzlore42`                            | <audio src="assets/minecraft/sounds/dvzlore42.ogg" controls></audio>                            | `neutral`         |
| `dvzlore43`                            | <audio src="assets/minecraft/sounds/dvzlore43.ogg" controls></audio>                            | `neutral`         |
| `dvzlore44`                            | <audio src="assets/minecraft/sounds/dvzlore44.ogg" controls></audio>                            | `neutral`         |
| `dvzlore45`                            | <audio src="assets/minecraft/sounds/dvzlore45.ogg" controls></audio>                            | `neutral`         |
| `daragorfirebreath`                    | <audio src="assets/minecraft/sounds/daragorfirebreath1.ogg" controls></audio>                   | `ambient`         |
| `introsong`                            | <audio src="assets/minecraft/sounds/introsong.ogg" controls></audio>                            | `neutral`         |
| `nisovin.rocketboots`                  | <audio src="assets/minecraft/sounds/nisovin.rocketboots.ogg" controls></audio>                  | `weather`         |
| `nisovin.voicewormhole`                | <audio src="assets/minecraft/sounds/nisovin.voicewormhole.ogg" controls></audio>                | `hostile`         |
| `nisovin.wandfire`                     | <audio src="assets/minecraft/sounds/nisovin.wandfire.ogg" controls></audio>                     | `weather`         |
| `nisovin.wandhit`                      | <audio src="assets/minecraft/sounds/nisovin.wandhit.ogg" controls></audio>                      | `weather`         |
| `nisovin.wormholeactivate`             | <audio src="assets/minecraft/sounds/nisovin.wormholeactivate.ogg" controls></audio>             | `weather`         |
| `nisovin.wormholefire`                 | <audio src="assets/minecraft/sounds/nisovin.wormholefire.ogg" controls></audio>                 | `weather`         |
| `nisovin.tinderflamedraw`              | <audio src="assets/minecraft/sounds/nisovin.tinderflamedraw.ogg" controls></audio>              | `weather`         |
| `nisovin.tinderflame`                  | <audio src="assets/minecraft/sounds/nisovin.tinderflame1.ogg" controls></audio>                 | `weather`         |
| `nisovin.voicerocketboots`             | <audio src="assets/minecraft/sounds/nisovin.voicerocketboots1.ogg" controls></audio>            | `hostile`         |
| `nisovin.voicetinderflame`             | <audio src="assets/minecraft/sounds/nisovin.voicetinderflame1.ogg" controls></audio>            | `hostile`         |
| `nisovinboltfire`                      | <audio src="assets/minecraft/sounds/nisovinboltfire1.ogg" controls></audio>                     | `weather`         |
| `nisovindeath`                         | <audio src="assets/minecraft/sounds/nisovindeath.ogg" controls></audio>                         | `ambient`         |
| `nisovinlaugh`                         | <audio src="assets/minecraft/sounds/nisovinlaugh1.ogg" controls></audio>                        | `record`          |
| `nisovinlowonmana1`                    | <audio src="assets/minecraft/sounds/nisovinlowonmana1.ogg" controls></audio>                    | `ambient`         |
| `nisovinlowonmana2`                    | <audio src="assets/minecraft/sounds/nisovinlowonmana2.ogg" controls></audio>                    | `ambient`         |
| `nisovinlowonmana3`                    | <audio src="assets/minecraft/sounds/nisovinlowonmana3.ogg" controls></audio>                    | `ambient`         |
| `roamindeath`                          | <audio src="assets/minecraft/sounds/roamindeath.ogg" controls></audio>                          | `ambient`         |
| `roaminflamethrower`                   | <audio src="assets/minecraft/sounds/roaminflamethrower.ogg" controls></audio>                   | `weather`         |
| `roaminheal`                           | <audio src="assets/minecraft/sounds/roaminheal.ogg" controls></audio>                           | `roaminheal`      |
| `roaminholypurifier1`                  | <audio src="assets/minecraft/sounds/roaminholypurifier1.ogg" controls></audio>                  | `record`          |
| `roaminholypurifier2`                  | <audio src="assets/minecraft/sounds/roaminholypurifier2.ogg" controls></audio>                  | `record`          |
| `roaminholypurifier3`                  | <audio src="assets/minecraft/sounds/roaminholypurifier3.ogg" controls></audio>                  | `record`          |
| `roaminholypurifier4`                  | <audio src="assets/minecraft/sounds/roaminholypurifier4.ogg" controls></audio>                  | `record`          |
| `roaminholypurifier5`                  | <audio src="assets/minecraft/sounds/roaminholypurifier5.ogg" controls></audio>                  | `record`          |
| `roaminlowonarmor1`                    | <audio src="assets/minecraft/sounds/roaminlowonarmor1.ogg" controls></audio>                    | `ambient`         |
| `roaminlowonarmor2`                    | <audio src="assets/minecraft/sounds/roaminlowonarmor2.ogg" controls></audio>                    | `ambient`         |
| `roaminlowonarmor3`                    | <audio src="assets/minecraft/sounds/roaminlowonarmor3.ogg" controls></audio>                    | `ambient`         |
| `roaminlowonmana1`                     | <audio src="assets/minecraft/sounds/roaminlowonmana1.ogg" controls></audio>                     | `ambient`         |
| `roaminlowonmana2`                     | <audio src="assets/minecraft/sounds/roaminlowonmana2.ogg" controls></audio>                     | `ambient`         |
| `roaminlowonmana3`                     | <audio src="assets/minecraft/sounds/roaminlowonmana3.ogg" controls></audio>                     | `ambient`         |
| `roaminoutofammo1`                     | <audio src="assets/minecraft/sounds/roaminoutofammo1.ogg" controls></audio>                     | `ambient`         |
| `roaminoutofammo2`                     | <audio src="assets/minecraft/sounds/roaminoutofammo2.ogg" controls></audio>                     | `ambient`         |
| `roaminoutofammo3`                     | <audio src="assets/minecraft/sounds/roaminoutofammo3.ogg" controls></audio>                     | `ambient`         |
| `roaminrecharged1`                     | <audio src="assets/minecraft/sounds/roaminrecharged1.ogg" controls></audio>                     | `ambient`         |
| `roaminrecharged2`                     | <audio src="assets/minecraft/sounds/roaminrecharged2.ogg" controls></audio>                     | `ambient`         |
| `roaminrecharged3`                     | <audio src="assets/minecraft/sounds/roaminrecharged3.ogg" controls></audio>                     | `ambient`         |
| `roaminrecharged4`                     | <audio src="assets/minecraft/sounds/roaminrecharged4.ogg" controls></audio>                     | `ambient`         |
| `goblinaction`                         | <audio src="assets/minecraft/sounds/goblinaction1.ogg" controls></audio>                        | `ambient`         |
| `goblinhurt`                           | <audio src="assets/minecraft/sounds/goblinhurt1.ogg" controls></audio>                          | `ambient`         |
| `goblindie`                            | <audio src="assets/minecraft/sounds/goblindie1.ogg" controls></audio>                           | `ambient`         |
| `goblinspawn`                          | <audio src="assets/minecraft/sounds/goblinspawn1.ogg" controls></audio>                         | `ambient`         |
| `goblinkaboomready`                    | <audio src="assets/minecraft/sounds/goblinkaboomready.ogg" controls></audio>                    | `ambient`         |
| `goblinkaboomfire`                     | <audio src="assets/minecraft/sounds/goblinkaboomfire.ogg" controls></audio>                     | `ambient`         |
| `ogredie`                              | <audio src="assets/minecraft/sounds/ogredie1.ogg" controls></audio>                             | `ambient`         |
| `ogreattack`                           | <audio src="assets/minecraft/sounds/ogreattack1.ogg" controls></audio>                          | `ambient`         |
| `ogrehurt`                             | <audio src="assets/minecraft/sounds/ogrehurt1.ogg" controls></audio>                            | `ambient`         |
| `ogrespawn`                            | <audio src="assets/minecraft/sounds/ogrespawn1.ogg" controls></audio>                           | `ambient`         |
| `storejimmy`                           | <audio src="assets/minecraft/sounds/storejimmy1.ogg" controls></audio>                          | `ambient`         |
| `monsterheroevent`                     | <audio src="assets/minecraft/sounds/monsterheroevent.ogg" controls></audio>                     | `ambient`         |
| `grand_paladin_authorization_required` | <audio src="assets/minecraft/sounds/grand_paladin_authorization_required.ogg" controls></audio> | `ambient`         |
| `musical.levelup`                      | <audio src="assets/minecraft/sounds/musical.levelup.ogg" controls></audio>                      | `ambient`         |
| `rat.laugh`                            | <audio src="assets/minecraft/sounds/rat.laugh.ogg" controls></audio>                            | `ambient`         |
| `bow.reload`                           | <audio src="assets/minecraft/sounds/bow.reload.ogg" controls></audio>                           | `ambient`         |
| `sword.prepare`                        | <audio src="assets/minecraft/sounds/sword.prepare.ogg" controls></audio>                        | `ambient`         |
| `musical.oldgods`                      | <audio src="assets/minecraft/sounds/musical.oldgods.ogg" controls></audio>                      | `ambient`         |
| `deathsound`                           | <audio src="assets/minecraft/sounds/deathsound.ogg" controls></audio>                           | `player`          |
| `sawmillaccident`                      | <audio src="assets/minecraft/sounds/sawmillaccident.ogg" controls></audio>                      | `player`          |