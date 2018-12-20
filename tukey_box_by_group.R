# Box and whisker plots with Tukey's Honestly Significant Differences groups
## Written by Noelle Patterson, 2018
library(multcompView)

# Set your working directory where you keep the input data
workingDir <- "/Users/noellepatterson/apps/FFC_bootstrapping/Outputs/tukey_wyt"
# workingDir <- "/Users/noellepatterson/apps/FFC_bootstrapping/Outputs/tukey/"
setwd(workingDir)

# ensure that file name is consistent with name below
input_file <- "tukey_input_bootstrapping.csv"

data_values <- read.csv(input_file, header = TRUE, check.names = FALSE, na.strings=c("","NA"))
tuk_df <- data.frame(data_values)
tuk_df <- tuk_df[(-2)] # remove class column from list of metrics
tuk_df <- filter(tuk_df,  groups == "WET" | groups == "DRY" | groups == "MODERATE")

# What groups are of interest to test significance between
# groups <- c("1-SM","2-HSR","3-LSR","4-WS","5-GW","6-PGR","7-FER","8-RGW","9-HLP")
groups <- c("WET", "MODERATE", "DRY")
groups <- as.factor(groups) 
# Assign your data matrix or dataframe
tuk_df$groups <- as.factor(tuk_df$groups)
metrics <- names(tuk_df)
metric_units <- c("Flow (cfs)","Flow (cfs)","Percent","Timing (Days)","Duration (Days)","Rate of Change (%)","Flow (cfs)","Timing (days)","Flow (cfs)","Flow (cfs)","Duration (Days)","Duration (Days)","Duration (Days)","Timing (Days)","Timing (Days)","Duration (Days)","Flow (cfs)","Flow (cfs)","Timing (Days)","Frequency (Days)","Duration (Days)","Flow (cfs)","Timing (Days)","Frequency (Days)","Duration (Days)","Flow (cfs)","Timing (Days)","Frequency (Days)","Duration (Days)","Flow (cfs)","Timing (Days)","Frequency (Days)","Duration (Days)","Flow (cfs)")

generate_label_df <- function(TUKEY){
  # Extract labels and factor levels from Tukey post-hoc 
  Tukey_levels <- TUKEY[["groups"]][,4]
  Tukey_labels <- data.frame(multcompLetters(Tukey_levels)["Letters"])
  #I need to put the labels in the same order as in the boxplot :
  Tukey_labels$treatment=rownames(Tukey_labels)
  Tukey_labels=Tukey_labels[order(Tukey_labels$treatment) , ]
  return(Tukey_labels)
}

# Loops through attributes/metrics
for (j in 1:(ncol(tuk_df)-1)) {
  # Box and whisker plots for chosen attributes/metrics
  # Attribute/metric name
  att_name <- names(tuk_df[j+1])
  # Formula for specific attribute as it relates to defined groups
  f <- paste(att_name, "~", "groups")
  aov_fit <- aov(as.formula(f), data=tuk_df) # analysis of variance
  
  # Tukey calculations based on aov.fit
  TUKEY <- TukeyHSD(aov_fit, "groups", conf.level = 0.95)
  LABELS=generate_label_df(TUKEY)
  metric_col <- tuk_df[,j+1]
  a=boxplot(metric_col ~ tuk_df$groups)
  a=boxplot(metric_col ~ tuk_df$groups, ylab=metric_units[j] , main=metrics[j+1], na.rm=TRUE, outline = FALSE, ylim = c(0,1.1*max(a$stats[nrow(a$stats),])))
  over=0.1*max(a$stats[nrow(a$stats),], na.rm=TRUE)
  text(c(1:nlevels(tuk_df$groups)) , a$stats[nrow(a$stats),]+over , LABELS[,1])
  dev.copy(png, filename = paste0("plot_", metrics[j+1], ".png"))
  dev.off()
}
