# Box and whisker plots with tukey's Honestly Significant Differences groups
## Written by Noelle Patterson, 2018
library(multcompView)
library(dplyr)

# Set your working directory where you keep the input data
# workingDir <- "/Users/noellepatterson/apps/FFC_QA/Outputs/"
workingDir <- "/Users/noellepatterson/apps/FFC_bootstrapping/Outputs/tukey_wyt/"
setwd(workingDir)

# ensure that file name is consistent with name below
input_file <- "tukey_input_bootstrapping.csv"

data_values <- read.csv(input_file, header = TRUE, check.names = FALSE, na.strings=c("","NA"))
tuk_df <- data.frame(data_values)

# If analyzing one wyt at a time, filter by that wyt and delete wyt column from metrics table
# tuk_df <- filter(tuk_df, groups == "MODERATE")
# tuk_df <- filter(tuk_df, class == "9_HLP")
# tuk_df <- tuk_df[(-1)] # remove wyt column from list of metrics

names(tuk_df)[2] <- "groups" # change for either WYT or class analysis

# uncomment for wyt analysis
tuk_df <- tuk_df[(-1)] # remove class column from list of metrics
# tuk_df <- filter(tuk_df,  groups == "WET" | groups == "DRY" | groups == "MODERATE") # remove NA rows from analysis

# What groups are of interest to test significance between
groups <- c("1_SM","2_HSR","3_LSR","4_WS","5_GW","6_PGR","7_FER","8_RGW","9_HLP") # 9-class boxplots, for wyt analysis
# groups <- c("WET", "MODERATE", "DRY") # 3-wyt boxplots, for class analysis
# groups <- c("1_Snowmelt", "2_Rain and Snowmelt", "3_Rain") # 3 broad hydro categories
groups <- as.factor(groups) 
# Assign your data matrix or dataframe
tuk_df$groups <- as.factor(tuk_df$groups)
metrics <- names(tuk_df)
metric_units <- c("Flow (cfs)","Flow (cfs)","Percent","Timing (Days since Oct 1st)","Duration (Days)","Rate of Change (%)","Flow (cfs)","Timing (Days since Oct 1st)","Flow (cfs)","Flow (cfs)","Duration (Days)","Duration (Days)","Duration (Days)","Timing (Days since Oct 1st)","Timing (Days since Oct 1st)","Duration (Days)","Flow (cfs)","Flow (cfs)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)","Frequency (Days)","Duration (Days)","Flow (cfs)")
# metric units below for select metrics to plot
# metric_units <- c("Flow (cfs)","Percent","Timing (Days since Oct 1st)","Timing (Days since Oct 1st)","Flow (cfs)","Duration (Days)","Duration (Days)","Timing (Days since Oct 1st)","Flow (cfs)","Frequency (Days)","Frequency (Days)","Flow (cfs)","Timing (Days since Oct 1st)")

generate_label_df <- function(tukey){
  # Extract labels and factor levels from tukey post-hoc 
  tukey_levels <- tukey[["groups"]][,4]
  tukey_labels <- data.frame(multcompLetters(tukey_levels)["Letters"])
  # put the labels in the same order as in the boxplot :
  tukey_labels$treatment=rownames(tukey_labels)
  tukey_labels=tukey_labels[order(tukey_labels$treatment) , ]
  return(tukey_labels)
}

# Create summary table of ncol=37 (classes) or ncol=4 (WYTs)
# summary_table <- data.frame(matrix("NA", ncol = 4, nrow = 43), stringsAsFactors=FALSE)
# headers <- rep(NA, length(names(tukey$groups[,1])))
# names <- names(tukey$groups[,1])
# for (i in 1:length(names)) {
#   headers[i] <- substring(names[i], 1, nchar(names))
#   headers[i] <- gsub("_", "", headers[i])
#   headers[i] <- gsub("\\d+", "", headers[i])
#   headers[i] <- gsub("-", "_", headers[i])
# }
# headers <- append('Metric', headers)
# names(summary_table) <- headers
# Loops through attributes/metrics
for (j in 1:(ncol(tuk_df)-1)) {
  # Box and whisker plots for chosen attributes/metrics
  att_name <- names(tuk_df[j+1])
  #Use if class = GW or HLP and column of 0's throws off the code
  # if (att_name == 'DS_No_Flow') {
  #   next
  # }
  # Formula for specific attribute as it relates to defined groups
  f <- paste(att_name, "~", "groups")
  aov_fit <- aov(as.formula(f), data=tuk_df) # analysis of variance
  
  # tukey calculations based on aov.fit
  tukey <- TukeyHSD(aov_fit, "groups", conf.level = 0.95)
  labels=generate_label_df(tukey)
  
  # Create a summary table with tukey letters for each metric
  # metric_vals <- tukey$groups[,4] # assign pair-wise p-vals to each row
  # summ_row <- data.frame(append(att_name, metric_vals), stringsAsFactors=FALSE)
  # summ_row <- append(att_name, metric_vals)
  # summary_table[j,] <- summ_row
  
  # define boxplot colors for 9-class or 3-wyt categories
  # colors = c("#FFCC00", "#93DB70", "#66CCFF") # "yellow", "green", "blue"
  colors = c("#FFCC00", "#000099", "#33FFFF", "#FF6600", "#CC0000", "#66CC00", "#FF6699", "#CC33FF", "#CC0099") # "yellow", "darkblue", "cyan", "orange", "red", "green", "pink", "purple", "magenta"
  metric_col <- tuk_df[,j+1]
  # width_sm <- length(which(tuk_df$groups=="1_Snowmelt")/length(tuk_df))
  # width_smr <- length(which(tuk_df$groups=="2_Rain and Snowmelt")/length(tuk_df))
  # width_rn <- length(which(tuk_df$groups=="3_Rain")/length(tuk_df))
  # proportion <- table(width_sm,width_smr,width_rn)
  
  a=boxplot(metric_col ~ tuk_df$groups)
  a=boxplot(metric_col ~ tuk_df$groups, ylab=metric_units[j], main=metrics[j+1], las=0, na.rm=TRUE, col=colors, las=0, outline = FALSE, ylim = c(0,1.1*max(a$stats[nrow(a$stats),])))
  # axis(2, at=c(0,73,146,219,292,365), labels=c('Oct','Jan','Apr','Jul','Jun','Oct'))
  # axis(2, at=c(0,60,122,183,244,305), labels=c('Oct','Jan','Apr','Apr','Jul','Oct'))
  # axis(2, at=c(0,30,61,91), labels=c('Oct','Nov','Jan','Feb'))
  over=0.1*max(a$stats[nrow(a$stats),], na.rm=TRUE)
  text(c(1:nlevels(tuk_df$groups)) , a$stats[nrow(a$stats),]+over , labels[,1])
  # setwd("/Users/noellepatterson/apps/FFC_bootstrapping/Outputs/tukey_wyt/tukey_by_wyt/wet")
  dev.copy(png, filename = paste0("plot_", metrics[j+1], ".png"))
  # dev.copy2pdf(file=paste0("plot_", metrics[j+1], ".pdf"), width=8,height=6)
  dev.off()
}

# setwd("/Users/noellepatterson/apps/FFC_bootstrapping/Outputs/Summary_tables/total")
# write.csv(summary_table, file="total.csv")

