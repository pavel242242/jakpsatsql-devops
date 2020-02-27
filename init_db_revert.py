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


#vytvoreni schemat a roli pro kazdy node
print ("--USER LOGIN, SCHEMA, ROLE")
for node in cg["NODES"]:
    n = node["NAME"]
    print ("" \
          "-- DROP SCHEMAT A ROLI NODE "+n+"; \n"          
          "DROP ROLE ROLE_"+n+"; \n" \
          "DROP ROLE ROLE_"+n+"_KOUC; \n" \
          "DROP SCHEMA SCH_"+n+"; \n"
          "DROP SCHEMA SCH_"+n+"_HRISTE; \n")
    lLogins = node["LOGINS"]
    for u in lLogins:
        print (" \n" \
        "DROP ROLE ROLE_"+n+"_"+u+";\n" \
        "DROP SCHEMA SCH_"+n+"_"+u+";\n" \
        "DROP USER "+n+"_"+u+"; \n" \
        )



#create schema $schema
# role
# ownership
# hriste
# testdata
# clenstvi v role_czechita
