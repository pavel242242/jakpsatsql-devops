cg={ \
  "NODES": [
    {"NAME" : "CZECHITA",
     "LOGINS" : ["01", "02"]
    },
    {"NAME" : "UK",
     "LOGINS" : ["01", "02"]
    },
    {"NAME" : "POKROCILI",
     "LOGINS" : ["01", "02"]
    }
],
"COACHES": [
      {"NAME"  : "ONDRA",
      "EMAIL" : "HOSAK@AVAST.COM"
      },
      {"NAME"  :"VERONIKA",
      "EMAIL" : "VERONIKA@GMAIL.COM"
      },
      {"NAME"  : "PAVLA",
      "EMAIL" : "JIRKOVA.PA@GMAIL.COM"
      },
      {"NAME"  : "OLGA",
      "EMAIL" : "OLGA.KURTINOVA@NATUR.CUNI.CZ"
      },
      {"NAME"  : "BUBLINA",
      "EMAIL" : "BUBLINA@SEZNAM.COM"
      }]
    }

#jeden kouc ;)
print ("CREATE ROLE ROLE_SUPERKOUC; \n" \
       "GRANT ROLE ROLE_SUPERKOUC TO USER CHOCHOLOUSP; \n"
       "CREATE ROLE ROLE_KOUC; \n" \
       "/ * * * * * * * *  * * * * **********************************/ \n"
      )
#a dalsi kouci
print ("--VYTVORENI KOUCU")
for c in cg["COACHES"]:
    u = c["NAME"]
    e = c["EMAIL"]
    print("CREATE OR REPLACE USER KOUC_"+u+" PASSWORD = 'SpANEKSeNePRECENUJE', EMAIL = '"+e+"', MUST_CHANGE_PASSWORD = TRUE, DEFAULT_WAREHOUSE = 'EXT_PROJECT', DEFAULT_NAMESPACE = 'CHOCHOLOUSP.PUBLIC', DEFAULT_ROLE = 'ROLE_KOUC';")
print("")
#create user ondra password = 'SPANEKSENEPRECENUJE', email = 'HOSAK@AVAST.COM', must_change_password = true, DEFAULT_WAREHOUSE = 'EXT_PROJECT', DEFAULT_NAMESPACE = 'CHOCHOLOUSP.PUBLIC', DEFAULT_ROLE = 'EXT_ADMIN';

#vytvoreni schemat a roli pro kazdy node
print ("--USER LOGIN, SCHEMA, ROLE")
for node in cg["NODES"]:
    n = node["NAME"]
    print ("" \
          "-- VYTVORENI SCHEMAT A ROLI NODE "+n+"; \n"          
          "CREATE ROLE ROLE_"+n+"; \n" \
          "CREATE ROLE ROLE_"+n+"_KOUC; \n" \
          "CREATE SCHEMA SCH_"+n+"; \n"
          "CREATE SCHEMA SCH_"+n+"_HRISTE; \n")
    lLogins = node["LOGINS"]
    for u in lLogins:
        print (" \n" \
        "CREATE ROLE ROLE_"+n+"_"+u+";\n" \
        "CREATE SCHEMA SCH_"+n+"_"+u+";\n" \
        "CREATE OR REPLACE USER "+n+"_"+u+" PASSWORD = 'SpANEKSePrECENUJE', MUST_CHANGE_PASSWORD = TRUE, DEFAULT_WAREHOUSE = 'EXT_PROJECT', DEFAULT_NAMESPACE = 'CHOCHOLOUSP."+n+"', DEFAULT_ROLE = 'ROLE_"+n+"'; \n" \
        )

#granty
for node in cg["NODES"]:
    n = node["NAME"]
    print ("-- GRANTNUTI PRAV KOUCUM PRO NODE "+n+"; \n"
           "GRANT ROLE ROLE_"+n+"_KOUC TO ROLE ROLE_SUPERKOUC; \n" \
     "GRANT ROLE ROLE_"+n+" TO ROLE ROLE_"+n+"_KOUC; \n" )
print(" /*UNCOMMENT AT WILL")
for node in cg["NODES"]:
    n = node["NAME"]
    print("-- ROLES FOR " + n)
    for c in cg["COACHES"]:
        u = c["NAME"]
        print ("" \
        "--GRANT ROLE_"+n+"_KOUC TO ROLE KOUC_"+u+"")
print("UNCOMMENT AT WILL */ \n")

print ("--GRANT SELECT ON SCHEMAS TO ROLES")
for node in cg["NODES"]:
    n = node["NAME"]
    print ("GRANT USAGE ON DATABASE COURSES TO ROLE ROLE_"+n+"; \n" \
    "GRANT USAGE ON SCHEMA SCH_"+n+" TO ROLE ROLE_"+n+"; \n" \
    "GRANT SELECT ON ALL TABLES IN SCHEMA SCH_"+n+" TO ROLE ROLE_"+n+"; \n" \
    "GRANT USAGE ON SCHEMA SCH_"+n+"_HRISTE TO ROLE ROLE_"+n+"; \n" \
    "GRANT SELECT ON ALL TABLES IN SCHEMA SCH_"+n+"_HRISTE TO ROLE ROLE_"+n+"; \n" \
    "GRANT ALL ON SCHEMA SCH_"+n+" TO ROLE ROLE_"+n+"_KOUC; \n"
    "GRANT ALL ON ALL TABLES IN SCHEMA SCH_"+n+" TO ROLE ROLE_"+n+"_KOUC; ")
    for u in node["LOGINS"]:
        print ("GRANT ROLE ROLE_"+n+" TO ROLE ROLE_"+n+"_"+u+";")

for node in cg["NODES"]:
    n = node["NAME"]
    for u in node["LOGINS"]:
        print ("GRANT ALL ON SCHEMA SCH_"+n+"_"+u+" TO ROLE ROLE_"+n+"_"+u+"; \n" \
        "GRANT ALL ON ALL TABLES IN SCHEMA SCH_"+n+"_"+u+" TO ROLE ROLE_"+n+"_"+u+"; \n" \
        "GRANT ALL ON SCHEMA SCH_"+n+"_"+u+" TO ROLE ROLE_"+n+"_KOUC; \n" \
        "GRANT ALL ON ALL TABLES IN SCHEMA SCH_"+n+"_"+u+" TO ROLE ROLE_"+n+"_KOUC;" )
#create schema $schema
# role
# ownership
# hriste
# testdata
# clenstvi v role_czechita
