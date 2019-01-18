library(tidyverse)
library(tidycensus)

# Requesting census data for target state.

# For NY, it's Barclays Center, opened 2012. We request from 20011-2016

ny_2011 <- get_acs(geography = "county",
                        variables =
                            c(hhincome = "B19013_001",
                              medage = "B01002_001",
                              poppoverty = "B05010_002",
                              popfoodstamps = "B22001_002",
                              popunemployed = "B23025_005",
                              totalpop = "B01003_001",
                              popwhite = "B02001_002",
                              popblack = "B02001_003",
                              popakna = "B02001_004",
                              popasian = "B02001_005",
                              pophipi = "B02001_006",
                              popother = "B02001_007",
                              pop2ormore = "B02001_008"),
                              state = "NY",
                              year =  2011,
                        output = "wide")

write.csv(ny_2011, file = "D:\\Stadiums Project\\NY data\\raw\\ny_2011.csv")

ny_2012 <- get_acs(geography = "county",
                        variables =
                            c(hhincome = "B19013_001",
                              medage = "B01002_001",
                              poppoverty = "B05010_002",
                              popfoodstamps = "B22001_002",
                              popunemployed = "B23025_005",
                              totalpop = "B01003_001",
                              popwhite = "B02001_002",
                              popblack = "B02001_003",
                              popakna = "B02001_004",
                              popasian = "B02001_005",
                              pophipi = "B02001_006",
                              popother = "B02001_007",
                              pop2ormore = "B02001_008"),
                              state = "NY",
                              year =  2012,
                        output = "wide")

write.csv(ny_2012, file = "D:\\Stadiums Project\\NY data\\raw\\ny_2012.csv")

ny_2013 <- get_acs(geography = "county",
                        variables =
                            c(hhincome = "B19013_001",
                              medage = "B01002_001",
                              poppoverty = "B05010_002",
                              popfoodstamps = "B22001_002",
                              popunemployed = "B23025_005",
                              totalpop = "B01003_001",
                              popwhite = "B02001_002",
                              popblack = "B02001_003",
                              popakna = "B02001_004",
                              popasian = "B02001_005",
                              pophipi = "B02001_006",
                              popother = "B02001_007",
                              pop2ormore = "B02001_008"),
                              state = "NY",
                              year =  2013,
                        output = "wide")

write.csv(ny_2013, file = "D:\\Stadiums Project\\NY data\\raw\\ny_2013.csv")

ny_2014 <- get_acs(geography = "county",
                        variables =
                            c(hhincome = "B19013_001",
                              medage = "B01002_001",
                              poppoverty = "B05010_002",
                              popfoodstamps = "B22001_002",
                              popunemployed = "B23025_005",
                              totalpop = "B01003_001",
                              popwhite = "B02001_002",
                              popblack = "B02001_003",
                              popakna = "B02001_004",
                              popasian = "B02001_005",
                              pophipi = "B02001_006",
                              popother = "B02001_007",
                              pop2ormore = "B02001_008"),
                              state = "NY",
                              year =  2014,
                        output = "wide")

write.csv(ny_2014, file = "D:\\Stadiums Project\\NY data\\raw\\ny_2014.csv")

ny_2015 <- get_acs(geography = "county",
                        variables =
                            c(hhincome = "B19013_001",
                              medage = "B01002_001",
                              poppoverty = "B05010_002",
                              popfoodstamps = "B22001_002",
                              popunemployed = "B23025_005",
                              totalpop = "B01003_001",
                              popwhite = "B02001_002",
                              popblack = "B02001_003",
                              popakna = "B02001_004",
                              popasian = "B02001_005",
                              pophipi = "B02001_006",
                              popother = "B02001_007",
                              pop2ormore = "B02001_008"),
                              state = "NY",
                              year =  2015,
                        output = "wide")

write.csv(ny_2015, file = "D:\\Stadiums Project\\NY data\\raw\\ny_2015.csv")

ny_2016 <- get_acs(geography = "county",
                        variables =
                            c(hhincome = "B19013_001",
                              medage = "B01002_001",
                              poppoverty = "B05010_002",
                              popfoodstamps = "B22001_002",
                              popunemployed = "B23025_005",
                              totalpop = "B01003_001",
                              popwhite = "B02001_002",
                              popblack = "B02001_003",
                              popakna = "B02001_004",
                              popasian = "B02001_005",
                              pophipi = "B02001_006",
                              popother = "B02001_007",
                              pop2ormore = "B02001_008"),
                              state = "NY",
                              year =  2016,
                        output = "wide")

write.csv(ny_2016, file = "D:\\Stadiums Project\\NY data\\raw\\ny_2016.csv")

ny_2017 <- get_acs(geography = "county",
                        variables =
                            c(hhincome = "B19013_001",
                              medage = "B01002_001",
                              poppoverty = "B05010_002",
                              popfoodstamps = "B22001_002",
                              popunemployed = "B23025_005",
                              totalpop = "B01003_001",
                              popwhite = "B02001_002",
                              popblack = "B02001_003",
                              popakna = "B02001_004",
                              popasian = "B02001_005",
                              pophipi = "B02001_006",
                              popother = "B02001_007",
                              pop2ormore = "B02001_008"),
                              state = "NY",
                              year =  2017,
                        output = "wide")

write.csv(ny_2017, file = "D:\\Stadiums Project\\NY data\\raw\\ny_2017.csv")

