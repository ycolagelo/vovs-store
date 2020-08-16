
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
