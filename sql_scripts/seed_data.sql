
-- Category
INSERT INTO "category" ("id","name") VALUES ('1','Electronics');
INSERT INTO "category" ("id","name") VALUES ('2','Clothing');
INSERT INTO "category" ("id","name") VALUES ('3','School/Office Supplies');


--
-- Add some products
--

-- Google Nest
INSERT INTO "product" ("id","name","price","active","created_date","category_id","description")
VALUES ('1','Google Nest Mini Gen2','69.99','1','1597539316','1',
'Meet Nest Mini, the speaker you control with your voice. Use your Google Assistant to play music from Spotify, YouTube Music, and more. Ask about the weather, news, or almost anything. Get personalized info like your schedule and commute. Set timers and alarms. And control your compatible smart devices.
Diameter: 98 mm (3.85”)
Height: 42 mm (1.65”)
Weight: 181g
Power cable: 1.5 m
Connectivity: Wi-Fi, Bluetooth & Chromecast Built-In
Power: 15 W power adaptor
Port: DC power jack');

INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('1','https://i5.walmartimages.ca/images/Enlarge/627/508/6000200627508.jpg','1','0');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('2','https://i5.walmartimages.ca/images/Enlarge/627/520/6000200627520.jpg','1','1');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('3','https://i5.walmartimages.ca/images/Enlarge/794/290/6000201794290.jpg','1','2');

-- Amazon Echo
INSERT INTO "product" ("id","name","price","active","created_date","category_id","description") VALUES ('2','Echo Dot (3rd gen) - Smart speaker with Alexa - Charcoal','34.95','1','1597543381','1','Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small spaces.
Improved speaker quality - Better speaker quality than Echo Dot Gen 2 for richer and louder sound. Pair with a second Echo Dot for stereo sound.
Voice control your music - Stream songs from Amazon Music, Apple Music, Sirius XM, Spotify, Deezer, and others. You can also listen to audiobooks from Audible.
Ready to help - Ask Alexa to play music, answer questions, read the news, check the weather, set alarms, control compatible smart home devices, and more.
Voice control your smart home - Turn on lights, adjust thermostats, lock doors, and more with compatible connected devices.
Connect with others - Call almost anyone hands-free. Instantly drop in on other rooms in your home or make an announcement to every room with a compatible Echo device.
Alexa has skills - With many skills and counting, Alexa is always getting smarter and adding new skills like checking your flight, playing games, and more.
Designed to protect your privacy - Built with multiple layers of privacy protections and controls, including a microphone off button that electronically disconnects the microphones.');

INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('4','https://images-na.ssl-images-amazon.com/images/I/419SVFEiGcL._AC_.jpg','2','11');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('5','https://images-na.ssl-images-amazon.com/images/I/61RNVt9kXUL._AC_SX679_.jpg','2','2');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('6','https://images-na.ssl-images-amazon.com/images/I/61WVZ3Dm5%2BL._AC_SL1000_.jpg','2','3');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('7','https://images-na.ssl-images-amazon.com/images/I/61fmA0M%2B8mL._AC_SL1000_.jpg','2','6');

-- Food box thing: back to school
INSERT INTO "product" ("id","name","price","active","created_date","category_id","description") VALUES ('3','Sistema To Go Collection Bento Box and Food Storage Container, 6.9 Cup, Clear, Assorted Color Klips','8.97','1','1597543895','3','Taking along a full lunch doesn''t have to mean carrying multiple food storage containers when you have the Sistema To Go Collection Bento Box. The plastic lunch box features multiple compartments that make it simple to keep your food fresh and separate until you''re ready to eat. There is a removable tray that is large enough to hold a sandwich, two hinged flip-top compartments ideal for sides like fruits and cheese, and a screw-top pot great for yogurt, pudding, salad dressing, sauce, and more. A lid with easy-locking clips and an extended flexible seal fits tightly over the bento lunch box to help keep items fresh. Made from 100% virgin plastic, this BPA- and phthalate-free bento box is dishwasher-safe when placed on the top rack, microwave-safe without the lids, and safe for storing in fridges and freezers.
• Bento lunch box takes the place of multiple plastic containers
• Lid with easy-locking clips and extended flexible seal helps keep contents fresh
• 100% virgin plastic; phthalate- and BPA-free
• Top-rack dishwasher-safe; fridge- and freezer-safe; microwave-safe without lids
• Includes removable sandwich tray, 2 hinged compartments, and 5-ounce/148-milliliter yogurt pot
• Note: This item will be received in assorted colours');

INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('8','https://i5.walmartimages.ca/images/Enlarge/131/376/6000199131376.jpg','3','0');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('9','https://i5.walmartimages.ca/images/Large/131/390/6000199131390.jpg','3','1');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES ('10','https://i5.walmartimages.ca/images/Enlarge/131/463/6000199131463.jpg','3','2');

-- Product 4
INSERT INTO "product" ("id","name","price","active","created_date","category_id","description","short_description") VALUES (4,'ABC Letters and Numbers Animal Card Board Matching Puzzle Game',23.77,1,'2020-08-24 17:06:36',3,'🌈Learning Letters & Numbers: Alphabets & Numbers Matching Cards Contains 36 flashcards(Alphabet A-Z and Number 1-10) and 36 smooth plastic blocks to correspond with the learning cards. Bright color and vivid picture can inspire your children''s interest in learning.
🌈Fun & Education Game: Kids find the corresponding letters by color and corresponding animals, For example, C corresponds to a Cat, The number corresponds to the same number of animals, Lively and interesting teaching of letters and numbers, Will make children learn better and know many animals.
🌈Benefit for Kids: Letter game can help children to develop eye-hand coordination, color recognition, fine motor skills, visual perception skills, problem-solving skills. Learn letters and numbers, as well as learn about animals and learn how to spell animals.
🌈Preschool Learning Toys: Great abc & 123 matching cards for toddlers. This toddler flash cards set for 3 year old is an interesting way to learn while playing, making children enjoy the fun of learning. Ideal for early educational learning Kindergarten toddlers & preschools.
🌈Child Safe: The alphabets and numbers teaching toy is made of safe, environmentally friendly, non-toxic, odorless BPA-free material as we value kids'' health, smooth edges keep your preschool boys and girls play safety.','');
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES (11,'https://images-na.ssl-images-amazon.com/images/I/71SiQmlVI9L._AC_SL1442_.jpg',4,1);
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES (12,'https://images-na.ssl-images-amazon.com/images/I/71XTUrpW5NL._AC_SL1464_.jpg',4,3);
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES (13,'https://images-na.ssl-images-amazon.com/images/I/71lp5CtMPAL._AC_SL1452_.jpg',4,2);

-- Product 5
INSERT INTO "product" ("id","name","price","active","created_date","category_id","description","short_description") VALUES (5,'Borescope Inspection Camera with Color LCD Screen',67.99,1,'2020-08-24 17:12:55',1,'【Upgraded Version & More Convenient Application】The pipe inspection monitor can probe any hard-to-reach areas, such as underwater or dark environments; A great tool for checking drains, pipelines, HAVC systems, car, boat and aircraft engines, air vent mechanical devices and more.
【HD LCD Display】2.31" LCD screen with 640 x 480 HD resolution, 2.0-megapixel CMOS, 8 levels of adjustable LED brightness, supports image rotation and contrast adjustment, help to reduce over expose and improve visibility in dark places, provide you with a better use experience.
【IP67 Waterproof & Universal Application】 IP67 Waterproof allows it to work in multiple environments, great for checking blocked drains, HAVC systems, car, boat and aircraft engines, mechanical devices and more.
【Sturdy and Durable】Semi-rigid snake camera tube for different shaping, textured handle for easy grip. Up to 6 hours of working hours to meet all your needs.
【Accessories Come in Handy】IP67 waterproof rated flexible tube and lens, 2 hooks, 2 rubber rings, magnet and mirror for various conditions, also a portable carrying toolbox for on the go.','');

INSERT INTO "product_image" ("id","url","product_id","priority") VALUES (14,'https://images-na.ssl-images-amazon.com/images/I/71A7XfMP-oL._SL1500_.jpg',5,1);
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES (15,'https://images-na.ssl-images-amazon.com/images/I/71--ODP-nKL._SL1500_.jpg',5,2);
INSERT INTO "product_image" ("id","url","product_id","priority") VALUES (16,'https://images-na.ssl-images-amazon.com/images/I/716vlhKnLEL._SL1500_.jpg',5,5);
