cg={ \
  "nodes": [
    {"name" : "czechita",
     "logins" : ["01", "02"]
    },
    {"name" : "uk",
     "logins" : ["01", "02"]
    },
    {"name" : "u3v",
     "logins" : ["01", "02"]
    }
],
"coaches": [
      {"name"  : "ondra",
      "email" : "hosak@avast.com"
      },
      {"name"  :"veronika",
      "email" : "hosak@avast.com"
      },
      {"name"  : "pavla",
      "email" : "hosak@avast.com"
      },
      {"name"  : "olga",
      "email" : "hosak@avast.com"
      },
      {"name"  : "bublina",
      "email" : "hosak@avast.com"
      }]
    }

for t in cg["coaches"]:
    print(t)

lLogins = ("01", "02")
lSlogins = ("ondra", "veronika", "pavla", "olga")
nodes = ("czechita", "uk", "pokrocili")

#jeden kouc ;)
print ("create role role_superkouc; \n" \
       "grant role role_superkouc to user chocholousp; \n"
       "/ * * * * * * * *  * * * * **********************************/ \n"
      )
#a dalsi kouci
for c in cg["coaches"]:
    u = c["name"]
    e = c["email"]
    print (" \n" \
    "create user "+u+" with_password = 'SpanekSeNeprecenuje', email = "+e+", must_change_password; \n")
#create user ondra password = 'SpanekSeNeprecenuje', email = 'hosak@avast.com', must_change_password = true, DEFAULT_WAREHOUSE = 'EXT_PROJECT', DEFAULT_NAMESPACE = 'CHOCHOLOUSP.PUBLIC', DEFAULT_ROLE = 'EXT_ADMIN';

#vytvoreni schemat a roli pro kazdy node
for node in cg["nodes"]:
    n = node["name"]
    print ("" \
          "-- Vytvoreni schemat a roli node "+n+"; \n"
          "create schema "+n+"; \n"
          "create role role_"+n+"; \n" \
          "create role role_"+n+"_kouc; \n" \
          "create schema sch_"+n+"_hriste; \n"
          "create schema "+n+"_hriste; \n")
    lLogins = node["logins"]
    for u in lLogins:
        print (" \n" \
  "create user "+n+"_"+u+" with_password = 'SpanekSePrecenuje', defaultnamespace, computenode, etc ...; \n" \
        "create role_"+n+"_"+u+";\n" \
        "create schema sch_"+n+"_"+u+";\n" )

#granty
for node in cg["nodes"]:
    n = node["name"]
    print ("-- grantnuti prav koucum pro node "+n+"; \n"
           "grant role role_"+n+"_kouc to role_superkouc; \n" \
     "grant role role_"+n+" to role_"+n+"_kouc; \n" )
print(" /*uncomment at will")
for node in cg["nodes"]:
    n = node["name"]
    print("-- roles for " + n)
    for c in cg["coaches"]:
        u = c["name"]
        print ("" \
        "--grant role_"+n+"_kouc to "+u+"")
print("uncomment at will */")

for node in cg["nodes"]:
    n = node["name"]
    print ("grant select on all tables in schema sch_"+n+" to role_"+n+"\n" \
    "grant all on schema sch_"+n+" to role_"+n+"_kouc; \n")
    for u in node["logins"]:
        print (" \n" \
        "grant role_"+n+" to role_"+n+"_"+u+"\n")

for node in cg["nodes"]:
    n = node["name"]
    for u in node["logins"]:
        print ("grant all on schema sch_"+n+"_"+u+" to role_"+n+"_"+u+";\n" \
         )
#create schema $schema
# role
# ownership
# hriste
# testdata
# clenstvi v role_czechita
