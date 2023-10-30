____________ google protocol buffers , protobuf, GPB nts : _______________________________
- from DBG-pri--2013-08

	_______:  ---
- see:
	http://code.google.com/p/protobuf/
	https://developers.google.com/protocol-buffers/docs/tutorials
	http://code.google.com/p/protobuf/downloads/list
##________________________________________  ___________________________


#####  ==========  DIFFs/DEFs:
	-!! DIFF:   protoFILE  <-->  message  <-->  message-class  <-->  protoFILE-class
		eg:  ProtoFile1.proto  <-->  Msg1 bzw. Msg2  <-->  Msg1.java  <-->  ProtoFile1.java /OR if java_outer_classname = "MsgPF1" then MsgPF1.java
		protoFILE	: xxx.proto text file for defining messages; very first file, which can contain several messages! (in kk-exp: ProtoFile1.proto with its java file defined as java_outer_classname = "MsgPF1")
		message	: one message defined in protoFILE. (in kk-exp: Msg1 bzw. Msg2 defined in  MsgPF1.proto)
		protoFILE-class	: protoc-generated java-file for the whole protoFILE.
		message-class	: protoc-generated java-file for each message inside a protoFILE. THis class+builder is included in protoFILE.java!
		- so after javac-compiling then the inner-/nested  message.java/classes are seen as seperate xx$yy.class files, but beforte that, they are includen as inner/nested classes inside  protoFILE.java!
##________________________________________  ___________________________


#####  ==========  extensions:
	--- writing-extension-fields, referencing extension in code (to write/set...) bzw. whom belong the extensions?:
		- if extension defined inside/embedded in a message, then it belongs as static member of the message!! as: m1.setExtension(Msg2.ext1Msg1InMsg2, i + 2000);
		- if extension defined directly in the protoFILE, then ProtoFILE.ext1 as in: m1.setExtension(MsgProtoFile1.ext2Msg1, i + 3000);
		-!! the extension-field belongs to the DEFINING message/protofile (see above), BUT the member-data/member-atribute/extension-itself belongs to the EXTENDED message!! so exp:
			message Msg2 { extend Msg1 {optional int32 ext1Msg1InMsg2=100 }}
			then m1 must be instance of Msg1:  Msg1.Builder m1 = Msg1.newBuilder();
			BUT the ext-filed belongs to the Msg2 for referencing (static member in Msg2):   m1.setExtension(Msg2.ext1Msg1InMsg2, 111);
	--- reading-extensions, referencing-by-reading:
		- by reading enc-files, either register ALL extensions defined inside a "protoFILE", even ones defined inside a message in this file, with protoFILE.registerAllExtensions(myregistry1) ! (too many no problem)
		-- or register individual extensions with:
		- if defined in a message:  ExtensionRegistry registry = ExtensionRegistry.newInstance();  registry.add(Msg2.ext1Msg1InMsg2); 	registry.add(MsgPF1.ext2Msg1);
		- if defined directly in the protoFILE (outside any messages), then: registry.add(MsgProtoFile1.ext1);
	--- registering-extensions:
		-! ONLY needed by reading! by writing just assign values to the filed if the message which contains the extension /OR of protoFile itself (see below)
		-! protoFILE.registerAllExtensions registers ALL extension for ALL messages defined in a protoFILE!! so the method is defined for a protoFILE!!
		-! NO problem if registering too many extensions! (eg with protoFILE.registerAllExtensions(myregistry1))
##________________________________________  ___________________________


#####  ==========  options:
	-! see  language-guide  : gpbdocs/0Refs_Tuts/language-guide_GPB.htm#options
	- listing of all options in:   ./src/google/protobuf/descriptor.proto   in dw-package!
	-! DIFF : opetion are defined for either protoFile/inseide.message/attribute/... !! so consider their context/constraints !!
##________________________________________  ___________________________


#####  ==========  INSTALL proto-compiler , setup as non-root:
	--- ofc1/lx4325 130821, gpb-2.4.1:
	tar -xzvf protobuf-2.4.1.tar.gz  -->
	cdlla /local/tempu1/varu/varau/ofc1var/gpb-241/protobuf-2.4.1
	./configure  --prefix=/local/.up1/optu/apps
	make ; make check ; make install
	test it:  protoc --version
	--- proto-compiler-setup (protoc)  on vo17-130317 as non-root-user, so as u1:
	unpacked in /up1/varu/varau/jvvar/resvar/ :
	tar -xzpvf /up1/w/docs/Javas/GoogleProtocolBuffer_GPBs/0Refs_GPBs/protobuf-2.5.0.tar.gz
	cd /up1/varu/varau/jvvar/resvar/protobuf-2.5.0/
	./configure --prefix=/up1/optu/apps
	make ; make check ; make install
	test it:  protoc --version
	-- java install:
	cd /up1/varu/varau/jvvar/resvar/protobuf-2.5.0/java
	mvn install
	so then:
	[INFO] Installing /mnt/VARUfs/varu_1204sus_vo17_Di3P8/varau/jvvar/resvar/protobuf-2.5.0/java/target/protobuf-java-2.5.0.jar to /home/u1/.m2/repository/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar
	[INFO] Installing /mnt/VARUfs/varu_1204sus_vo17_Di3P8/varau/jvvar/resvar/protobuf-2.5.0/java/pom.xml to /home/u1/.m2/repository/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.pom
	--> protobuf-java-2.5.0.jar must be in your classpath for your java-GPB-apps !!
	-- utils.adds:
	cp  ./editors/proto.vim   /up1/.cuue/etc/vims/syntax  + ~/.vim/ftdetect/proto.vim  :  see ./editors/proto.vim
	eclipse-plugin Protocol Buffer Editor , com.google.eclipse.protobuf.feature.group , 
##________________________________________  ___________________________


#####  ==========  default-GPB-values:
	- see  java-tutorial_GBP.html --> "Defining Your Protocol Format" + "Extending a Protocol Buffer":
	-! is only relevant for optional fields.
	- GPB-predefined-default-values: If the default value is not specified for an optional element, a type-specific default value is used instead: for strings, the default value is the empty string. For booleans, the default value is false. For numeric types, the default value is zero. Note also that if you added a new repeated field, your new code will not be able to tell whether it was left empty (by new code) or never set at all (by old code) since there is no has_ flag for it.
	- optional fields default values: the field may or may not be set. If an optional field value isn't set, a default value is used. For simple types, you can specify your own default value, as we've done for the phone number type in the example. Otherwise, a system default is used: zero for numeric types, the empty string for strings, false for bools. For embedded messages, the default value is always the "default instance" or "prototype" of the message, which has none of its fields set. Calling the accessor to get the value of an optional (or required) field which has not been explicitly set always returns that field's default value.
	- repeated fields: just empty as dafult
	- [default = xxx] : user-defined default values for optional fields as in:  optional int32 field1 = 20 [default = xxx]
##________________________________________  ___________________________


#####  ==========  api-javadoc-generation (including TEST-files ; here for ver.2.4.1):
	cdll ./protobuf-2.4.1/java ;  mkdir -p api.241_gen_gpb/main ; mkdir -p api.241_gen_gpb/test ;
	javadoc -d ./api.241_gen_gpb/main/   -sourcepath ./src/main/java/  com.google.protobuf
	javadoc -d ./api.241_gen_gpb/test/   -sourcepath ./src/test/java/  com.google.protobuf	
	(viorg api.241_gen_gpb/test/*css ;  viorg api.241_gen_gpb/main/*css)
	/OR both together:    javadoc -d ./api.241_gen_gpb/  -sourcepath  ./src/main/java/:./src/test/java/   com.google.protobuf
--###################### coll-done-130300 : ####################################
##________________________________________  ___________________________


#####  ==========  generating java-source-files from protos in a dir-TREE: 130821-ofc1-lx4325--CP (see prj-telo_ts):
	-! NOT-working something like " protoc  --java_out=./cil-protos-gen-1/  -I=./protos/   ./protos/CIL/*proto " ! :
	   protoc does NOT traverse the tree/dir !! so in this case, only xx.protos directly in ./protos/CIL/ where be compiled and NOT the tree!
	-- alle these tree worked the same and ok:
	- with find:   protoc  --java_out=./cil-protos-gen-3/  -I=./protos/  $(find ./protos -iname "*.proto")
	- all DIRs in the tree specified:  protoc  --java_out=./cil-protos-gen-1/  -I=./protos/  protos/CIL/*proto  protos/CIL/CIL_v001/Common/*proto  protos/CIL/CIL_v001/Eurex_v001/Common/*proto  protos/CIL/CIL_v001/Eurex_v001/Messages/*proto
	- eaxh DIr einzelne compiled from lower dependency to higher. so first: protoc  --java_out=./cil-protos-gen-1/  -I=./protos/  protos/CIL/*proto #-and then next,...
##________________________________________  ___________________________


#####  ==========  loaderProtos1-try1:

	- generate a pom-start-project /OR copy app2 there ...
	- cp loader-prots ~/.../work1/loader_protos_bindings/common_protobuf_Eurex_v001/cilmsg/src/CIL/   to  ./src/main/resources/protos/
	- not-worked:  protoc   --proto_path=.:${PROTO_SRC_RTDP1}:  --java_out=${PROTO_GEN_DST_DIR1}  ${PROTO_SRC_RTDP1}/*.proto
	so einzelne:  as in -->    ./common_protobuf_Eurex_v001/cilmsg/examples/test-proto-files-java.bat   :
	protoc --java_out=./src/main/gen/protogen/   -I=./src/main/resources/protos    ./src/main/resources/protos/CIL/*.proto
	protoc --java_out=./src/main/gen/protogen/   -I=./src/main/resources/protos    ./src/main/resources/protos/CIL/CIL_v001/*.proto
	protoc --java_out=./src/main/gen/protogen/   -I=./src/main/resources/protos    ./src/main/resources/protos/CIL/CIL_v001/Common/*proto
	protoc --java_out=./src/main/gen/protogen/   -I=./src/main/resources/protos    ./src/main/resources/protos/CIL/CIL_v001/Eurex_v001/Common/*proto
	protoc --java_out=./src/main/gen/protogen/   -I=./src/main/resources/protos    ./src/main/resources/protos/CIL/CIL_v001/Eurex_v001/Messages/*proto
	--> check them if importable: protoc --java_out=./src/main/gen/protogen/   -I=./src/main/resources/protos    ./src/main/resources/protos/CIL/test-eurex.proto
##________________________________________  ___________________________


#####  ==========  try3-offc--new.AB.org--basic.new (olds moved to tr), 130326: 
	- eclipse-app as: gpb1 in package org.pkg1.gpb

	_______:  make-tree/structure/maven-tree:
	[~/ws_wk1 -lx4325]$  mvn  archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-quickstart  -DgroupId=org.pkg1.gpb  -DartifactId=gpb1 -Dversion=1.0-SNAPSHOT -Dpackage=org.pkg1.gpb
	[~/ws_wk1/gpb1 -lx4325]$mkdir -p ./src/main/resources/protos
	[~/ws_wk1/gpb1 -lx4325]$mkdir -p ./src/main/gen/protogen

	_______:  add dependencies to pom.xml:
	vi  pom.xml  --> add: protobuf.jar-dependency + gen/protogen-src-dir to sources:
	- <dependency> <groupId>com.google.protobuf</groupId> <artifactId>protobuf-java</artifactId> <version>2.5.0</version> <scope>compile</scope> </dependency>
	- <build> <sourceDirectory>src/main/java</sourceDirectory> <plugins> <plugin> <groupId>org.codehaus.mojo</groupId> <artifactId>build-helper-maven-plugin</artifactId> <version>1.7</version> <executions> <execution> <id>add-source</id> <phase>generate-sources</phase> <goals> <goal>add-source</goal> </goals> <configuration> <sources> <source>src/main/gen/protogen</source> </sources> </configuration> </execution> </executions> </plugin> </plugins> </build>

	_______:  proto files (put/copy them to ./src/main/resources/protos ; either from examples or CIL, ...; here org-examples):
	- [.../protobuf-2.5.0/examples -lx4325]$  cp  addressbook.proto  /home/kampkur/ws_wk1/gpb1/src/main/resources/protos/
	in examples-case, also list/add.java-files:
	[.../protobuf-2.5.0/examples -lx4325]$cp *.java    ./src/main/java/
	   /OR?: adapt package-names and put in if like:  /home/kampkur/ws_wk1/gpb1/src/main/java/org/pkg1/gpb/
	- adapt package-imports in java-files ... /OR if want keep orgs, then not. ...

	_______:  protoc: generate proto-java-files:
	- [~/ws_wk1/gpb1 -lx4325]$protoc -I=.:./src/main/resources/protos/  --java_out=./src/main/gen/protogen/   ./src/main/resources/protos/*.proto
	-? if like: add protoc-task (as antrun-task) to pom.xml ? /OR just do it manually...

	_______:  manually compile/run -OK:
	- export protobuf_jar_DP1=/home/kampkur/maven-repo/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar
	- javac -cp  .:./target/classes/:${protobuf_jar_DP1}:${CLASSPATH}:   -sourcepath ./src/main/java/:./src/main/gen/protogen/:  -d ./target/classes/   ./src/main/java/*.java
	- java  -cp  .:./target/classes/:${protobuf_jar_DP1}:${CLASSPATH}:    AddPerson   f1.gpb
	- java  -cp  .:./target/classes/:${protobuf_jar_DP1}:${CLASSPATH}:    ListPeople  f1.gpb
		-?? /OR if prefered??: export CLASSPATH=.:/home/kampkur/maven-repo/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar:${CLASSPATH}: )  #BUT maybe better for now with -cp param!

	_______:  eclipse-run/import-maven-project:
	- import : existing-maven-project
	- check configs: source-dir,...
	- run-configure: args[0] : f1.gpb
	- run add + list

	_______:  ------------------------

	_______:  checking f1.gpb:
	strings / file / cat / vi  f1.gpb
--############################### coll: mvn.gpb, gpb,.... ##############################
##________________________________________  ___________________________


#####  ==========  maven task for GPB-source-generation / protoc ...:
// http://stackoverflow.com/questions/1578456/integrate-protocol-buffers-into-maven2-build :
 <build>
   <plugins>
     <plugin>
       <artifactId>maven-antrun-plugin</artifactId>
       <executions>
         <execution>
           <id>generate-sources</id>
           <phase>generate-sources</phase>
           <configuration>
             <tasks>
               <mkdir dir="target/generated-sources"/>
               <exec executable="protoc">
                 <arg value="--java_out=target/generated-sources"/>
                 <arg value="src/main/protobuf/test.proto"/>
               </exec>
             </tasks>
             <sourceRoot>target/generated-sources</sourceRoot>
           </configuration>
           <goals>
             <goal>run</goal>
           </goals>
         </execution>
       </executions>
     </plugin>
   </plugins>
 </build>
 <dependencies>
   <dependency>
     <groupId>com.google.protobuf</groupId>
     <artifactId>protobuf-java</artifactId>
     <version>2.0.3</version>
   </dependency>
 </dependencies>
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  codes.coll.adressbook.exp:
-! onliner add-persons to adressbook:
		Person.PhoneNumber.Builder phone1= Person.PhoneNumber.newBuilder().setNumber("31333").setType(PhoneType.MOBILE);
		addressBook.addPerson(Person.newBuilder().setId(31).setName("n31").setEmail("em31").addPhone(phone1));
--######################################### prev-old-trys-offc: ##############################################
##________________________________________  ___________________________


#####  ==========  try2-in eclipse ws_wk1:
[kampkur@lx4325 app1]$pwd
/home/kampkur/ws_wk1/gpb1/app1
[kampkur@lx4325 app1]$date
Mon Mar 18 10:38:49 CET 2013
[kampkur@lx4325 app1]$
[kampkur@lx4325 app1]$export  SRC_DIR1=./src/main/resources/protos/    DST_DIR1=./src/main/gen/   PROTO_DIR1=${SRC_DIR1}
[kampkur@lx4325 app1]$protoc  --proto_path=.:${SRC_DIR1}:  --java_out=${DST_DIR1}     ${PROTO_DIR1}/*.proto
--
[kampkur@lx4325 examples]$pwd
/var/tmp/.up1/varu/varau/docsvar/gpbdocsvar/protobuf-2.5.0/examples
[kampkur@lx4325 examples]$export CLASSPATH=.:/home/kampkur/maven-repo/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar:${CLASSPATH}:
make java
/OR:  cp  *.java  /home/kampkur/ws_wk1/gpb1/app1/src/main/java/org/pkg1/gpb1/app1/ ;
      cdlla .....app1;  mvn clean install ; #...
-- for eclipse + maven:
	- add ./src/main/gen/ to source
	-! modify pom.xml : add dependencies <groupId>com.google.protobuf</groupId> <artifactId>protobuf-java</artifactId> 
	  and also aditional src-dir <groupId>org.codehaus.mojo</groupId>  <artifactId>build-helper-maven-plugin</artifactId> .....
##________________________________________  ___________________________


#####  ==========  try1.dummy.only.proto: 
Fri Mar 15 11:21:03 CET 2013
[kampkur@lx4325 app1]$pwd
/var/tmp/.up1/.prjs/ofc1/wks/gpb1/app1
-- compile-proto-files (generate .java files):   proto --> java :
[kampkur@lx4325 app1]$protoc -I=./protos  --java_out=./src/main/java   ./protos/addressbook.proto 
-- compile-java-file (generate java.classes):   .java --> .class :
[kampkur@lx4325 app1]$javac -sourcepath ./src/main/java/  -cp /home/kampkur/maven-repo/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar -d /var/tmp/tempu1/prjs/ofc1/wks/gpb1/app1/target/classes  ./src/main/java/com/example/tutorial/AddressBookProtos.java
-- run (not-ok):
[kampkur@lx4325 classes]$java -cp /home/kampkur/maven-repo/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar  com.example.tutorial.AddressBookProtos
Error: Could not find or load main class com.example.tutorial.AddressBookProtos
##________________________________________  ___________________________


#####  ==========  try1.home-vo17-GPB-app1:
	- prj in:  /home/u1/ws_t1/gpb1/app1  :
	./protobuf-2.5.0/examples$  cp addressbook.proto ~/ws_t1/gpb1/app1/src/main/resources/
	u1@vo17:~/ws_t1/gpb1/app1 $   export SRC_DIR="./src/main/java/"   DST_DIR="./src/main/gen/"
	u1@vo17:~/ws_t1/gpb1/app1 $protoc --proto_path=$SRC_DIR:./src/main/resources:.  --java_out=$DST_DIR  ./src/main/resources/addressbook.proto
	  (proto-file must be also in proto_path!!)
