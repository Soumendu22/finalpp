BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "faculty" (
	"id"	INTEGER,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "attable" (
	"subid"	INTEGER,
	"subject"	TEXT,
	"attended"	INTEGER,
	"bunked"	INTEGER,
	"percentage"	NUMERIC,
	"id"	int,
	FOREIGN KEY("id") REFERENCES "users"("id"),
	PRIMARY KEY("subid")
);
CREATE TABLE "sqlite_sequence" (
	"name"	,
	"seq"	
);
INSERT INTO "users" ("id","username","password","email") VALUES (1,'soumendu','b7791f63c6254a1bb648d7fd3bba89b509ac00e4d325e0a56b9aacddb43a69b8','dhsadsAfjsdj'),
 (2,'Soumendu','505843b668b35e248a617477ea71125bffb149cd02a23e634d8957513784ce62','smanna22@ggg'),
 (3,'','e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',''),
 (4,'sam','e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605','sam@tam'),
 (5,'sam1','e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605','sdasdfas'),
 (6,'sam2','5bc9db7a666fcf9d04585ca5d194274cd5c0587644cb93249e0bbbe2aa6305e7','dsgdsgsd'),
 (7,'sam3','a47c3d2fb0d7d6385200b3f27e4b81ab77a6f0032b564df8c6ae5e2536b35b78','dsadasd'),
 (8,'sam5','e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605','sam@tam'),
 (9,'sam6','e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605','dshdjk@dsfsd'),
 (10,'sam7','e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605','sam@tam'),
 (11,'fdgdf','58ce792f00f34a7cbc92833ae23ced39c417c36e7869722df77ee62366e971db','dsgsdfgs@'),
 (12,'grefg','86cd050d61a65688206793d34ed5ba8dd185690b535c709bba67bff550cee39f','dsdsf@dfsgvfd'),
 (13,'sam10','e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605','sam@tam'),
 (14,'fdjsg','663d0a90bd7b50062b852fd48d915dee1805876ae0cbb7981adae0297a1c4529','sdfd@'),
 (15,'dsgdsg','e7eabc6e6c9370b96eb257acb267f6458383832689f2d42fddd79880c8bf52f7','dfASd@dsvdsf'),
 (16,'dsfds','3073f5e5796be025543ff5eba94bcf8610a5e323ffb2a0fc302ce3905ded8ec5','234@'),
 (17,'Your username','5746e1f1ede68802a24f194420ec0a950a6cbf89c242589f3c5ec772b00267a0','cdsfsd@sdc'),
 (18,'sds','5746e1f1ede68802a24f194420ec0a950a6cbf89c242589f3c5ec772b00267a0','hh@');
INSERT INTO "faculty" ("id","username","password","email") VALUES (1,'sam','e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605','sam@123');
INSERT INTO "attable" ("subid","subject","attended","bunked","percentage","id") VALUES (1,'a',3,5,37.5,NULL),
 (2,'b',0,0,0,NULL);
COMMIT;
