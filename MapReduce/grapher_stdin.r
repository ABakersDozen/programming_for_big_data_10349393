library(ggplot2)
dat <- read.csv(file="stdin", header=F, sep="\t")
#dat
words <- dat[1]
#words
count <- dat[2]
#count
ggplot(data=dat, aes(x=words, y=count)) +
    geom_bar(stat="identity") +
    scale_*_discrete()