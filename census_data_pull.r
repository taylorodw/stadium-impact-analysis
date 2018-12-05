library(tidycensus)

Sys.getenv("18bf09098f16d9a37caafd534edec5f1452ba8d1")

cali_request <- get_acs(geography = "county", 
                        variables = 
                            c(hhincome = "B19013_001", 
                              medage = "B01002_001", 
                              poppoverty = "B05010_002", 
                              totalpop = "B01003_001", 
                              popwhite = "B02001_002", 
                              popblack = "B02001_003", 
                              popakna = "B02001_004", 
                              popasian = "B02001_005", 
                              pophipi = "B02001_006", 
                              popother = "B02001_007", 
                              pop2ormore = "B02001_008"), 
                              state = "CA", 
                        output = "wide")

head(cali_request)

write.csv(cali_request, file = "/Users/kai/Documents/Projects/Stadium_analysis/testdata.csv")