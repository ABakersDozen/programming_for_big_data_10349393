#### set the working directory here ######

setwd("C:/Users/macan/programming_for_big_data_10349393/CA4") 

####### end wd #############

library(ggplot2)
# read in csv file
dat <- read.csv(file="ttest.csv", sep=",", header = F)
# name the columns
names(dat) <- c("Revision", "Author", "Timestamp","Lines in Comment","Commits","Comment")

# rename a long 'author' name with something slightly more meaningful
dat$Author <- factor(gsub("/OU=Domain Control Validated/CN=svn.company.net", "Domain Control Validated", dat$Author))

# some informative data about our dataframe. Helps to identify early points of analysis
str(dat)
summary(dat)


##### interesting statistical observation No. 1 ####
authors.freq <- sort(table(dat$Author),decreasing = TRUE) 

# barplot with perpendicular x-axis labels. 60deg looks better, see below
#barplot(authors.freq,main="Frequency of Author revisions",ylab="Frequency",xlab="Author Name",las=3)


par(mar = c(7, 4, 2, 2) + 1) #add room for the rotated labels
end_point = .5 + nrow(authors.freq) + nrow(authors.freq)-1 #this is the line which does the trick (together with barplot "space = 1" parameter)

barplot(authors.freq, col="grey50", 
        main="Frequency of Author revisions",
        ylab="Frequency", ylim=c(0,200),
        xlab = "",
        xaxt = "n",
        space=1)
#rotate 60 degrees, srt=60
text(seq(1.5,end_point,by=2), par("usr")[3]-0.25, 
     srt = 60, adj= 1.1, xpd = TRUE,
     labels = paste(rownames(authors.freq)), cex=0.8)

####### add some extra columns using the timestamp ########
dat$Date <- as.Date(dat$Timestamp)
dat$Day <- weekdays(dat$Date)
dat$Month <- format(dat$Date, "%B")
dat$Time <- format(as.POSIXct(dat$Timestamp),format = "%H:%M:%S")
month.freq <- summary(factor(dat$Month, levels = c("July", "August", "September", "October", "November")))
day.freq <- summary(factor(dat$Day, levels = c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")))

##### interesting statistical observation No. 2 ####
## commit occurances by day ##
barplot(day.freq, col="grey50", 
        main="Frequency of revisions by day",
        ylab="Frequency", ylim=c(0,150),
        xlab = "",
        las = 2)

##### interesting statistical observation No. 3 ####
## commit occurances by month ##
df <- as.data.frame(month.freq)
names(df) <- c("Frequency")
df$names <- factor(rownames(df), as.character(rownames(df)))

ggplot(df, aes(x=names, y=Frequency)) + 
  geom_bar(aes(x=names), data=df, stat="identity") + 
  labs(y="Frequency",x="Month",title="Frequency of revisions by month")


