# misc utils

def_par_allcomb = function(defpars) {
  npars = lapply(X = defpars, FUN = function(X) {out = length(X[[3]]); return(out)})
  if (!any(npars > 1)) {
    cat("No pars to combine")
    return(defpars)
  }
  pars_mult = sapply(defpars[npars>1], "[[", 3)
  pars_comb = expand.grid(as.list(unname(data.frame(pars_mult))))
  defpars[npars>1] = mapply(function(X, Y) {X[[3]] = Y; return(X)}, defpars[npars>1], pars_comb, SIMPLIFY = F)
  defpars[npars==1] = lapply(pars_list[npars==1], function(X, Y) {X[[3]] = rep.int(X[[3]], Y); return(X)}, length(pars_comb[[1]]))
  cat("Output def pars length: ", length(pars_comb[[1]]))
  return(defpars)
}

dup_soil_pars = function(input_def_pars, input_hdr) {
  par_df = as.data.frame(t(sapply(input_def_pars, function(X){X[1:2]})))
  par_df$values = lapply(input_def_pars,"[[", 3)
  if (length(input_hdr$soil_def) <= 1) {
    cat("One or less soil definition files listed in input header, cannot duplicate soil def pars.")
    return(input_def_pars)
  }
  if (length(input_hdr$soil_def) > 1 & all(input_hdr$soil_def %in% par_df$V1)) {
    cat("Multiple soil definition files already being modified in input definition pars, don't want to overwrite/unclear which to dup.")
    return(input_def_pars)
  }
  soil_i = which(par_df$V1 %in% input_hdr$soil_def)
  def_cur = input_hdr$soil_def[input_hdr$soil_def %in% par_df$V1]
  def2dup = input_hdr$soil_def[!input_hdr$soil_def %in% par_df$V1]
  pars_added = lapply(def2dup, function(def2dup, cur_pars) {
    lapply(cur_pars, function(X,Y) {X[[1]] = Y; return(X)},def2dup)
  }, cur_pars = input_def_pars[soil_i])
  new_input_def_pars = c(input_def_pars, unlist(pars_added, recursive = F))
  return(new_input_def_pars)
}

get_basin_daily = function(out_dir) {
  basin_files_in = list.files(path = out_dir, pattern = ".*_basin.daily", full.names = T)
  run_names = gsub("_basin", "", gsub(".csv", "", basename(basin_files_in)))
  basin_daily_list = lapply(basin_files_in, fread)
  basin_daily_list = mapply(function(X,Y) {X$run = Y;return(X)} , basin_daily_list, run_names, SIMPLIFY = F)
  basin_daily_dt = rbindlist(basin_daily_list)
  basin_daily_dt = add_dates(basin_daily_dt)
  return(basin_daily_dt)
}

cal_eval = function(out_dir, Qobs, monthly = F) {
  sim_DT = get_basin_daily(out_dir)
  print(head(sim_DT))
  min_comb = max(min(sim_DT$date), min(Qobs$date))
  max_comb = min(max(sim_DT$date), max(Qobs$date))
  Qobs = Qobs[Qobs$date >= min_comb & Qobs$date <= max_comb,]
  sim_DT = sim_DT[sim_DT$date >= min_comb & sim_DT$date <= max_comb,]
  sim_DT$streamflow = sim_DT$streamflow * 471402723.133291 ##basin size
  run_IDs = unique(sim_DT$run)
  print(run_IDs)
  #run_IDs = run_IDs[order(as.numeric(gsub("[^0-9]+_", "",run_IDs)))] #
  
  if (monthly) {
    sim_DT_mn = aggregate(sim_DT$streamflow, by = list(sim_DT$run, sim_DT$year, sim_DT$month), FUN = mean)
    names(sim_DT_mn) = c("run", "year","month","streamflow")
    Qobs$year = as.numeric(format(Qobs$Date, "%Y"))
    Qobs$month = as.numeric(format(Qobs$Date, "%m"))
    Qobs_mn = aggregate(Qobs$Flow_mmd, by = list(Qobs$year, Qobs$month), FUN = mean)
    names(Qobs_mn) = c("year","month","Flow_mmd")
    
    eval_fun_mn = function(i) {
      nse = NSE(sim_DT_mn[sim_DT_mn$run == i, "streamflow"], Qobs_mn$Flow_mmd)
      r = summary(lm(Qobs_mn$Flow_mmd ~ sim_DT_mn[sim_DT_mn$run == i, "streamflow"] ))$r.squared
      pbias = hydroGOF::pbias(Qobs_mn$Flow_mmd,sim_DT_mn[sim_DT_mn$run == i, "streamflow"])
      return(list(i, nse, r, pbias))
    }
    eval_list = lapply(run_IDs, FUN = eval_fun_mn)
    eval_df = rbindlist(eval_list)
    names(eval_df) = c("run", "NSE", "R2", "PBIAS")
    return(eval_df)
  }
  
  eval_fun = function(i) {
    nse = NSE(sim_DT[sim_DT$run == i, streamflow], Qobs$Flow_mmd)
    r = summary(lm(Qobs$Flow_mmd ~ sim_DT[sim_DT$run == i, streamflow] ))$r.squared
    pbias = hydroGOF::pbias(Qobs$Flow_mmd,sim_DT[sim_DT$run == i, streamflow])
    return(list(i, nse, r, pbias))
  }
  eval_list = lapply(run_IDs, FUN = eval_fun)
  eval_df = rbindlist(eval_list)
  names(eval_df) = c("run", "NSE", "R2", "PBIAS")
  return(eval_df)
}



read_def = function(def_file) {
  def_read = readLines(def_file, warn = FALSE)
  def_read = def_read[nchar(def_read) > 0]
  def_table_list =  strsplit(trimws(def_read), "\\s+")
  def_table <- as.data.frame(do.call(rbind, lapply(def_table_list, `length<-`, 2)), stringsAsFactors = FALSE)
  names(def_table)[1:2] = c("pars", "names")
  comments = lapply(def_table_list, function(x)ifelse(length(x) > 2, paste(x[3:length(x)], collapse = " "), NA ) )
  def_table_out = data.frame(def_table, comments = unlist(comments))
  return(def_table_out)
}

add_dates = function(DF){
  if ("day" %in% colnames(DF)) {
    DF$date = lubridate::ymd(paste(DF$year, DF$month, DF$day, sep = "-"))
    DF$wy = data.table::fifelse(DF$month >= 10, DF$year + 1, DF$year)
    DF$yd = lubridate::yday(DF$date)

    # need to account for varing numbers of patches etc so line offsets are wrong
    # yd = lubridate::yday(c(DF$date, seq.Date(DF$date[length(DF$date)], by = "day", length.out = 93)[2:93]))
    # DF$yd = yd[1:(length(yd) - 92)]
    # DF$wyd = yd[93:length(yd)]

    # wy_date = c(clim$date[93:length(clim$date)], seq.POSIXt(from = clim$date[length(clim$date)], by = "DSTday", length.out = 93)[2:93])
    # clim$wyd = lubridate::yday(wy_date)

  } else if (!"day" %in% colnames(DF) & "month" %in% colnames(DF)) {
    DF$wy = data.table::fifelse(DF$month >= 10, DF$year + 1, DF$year)
    DF$yr_mn = zoo::as.yearmon(paste(DF$year, DF$month, sep = "-"))

  }
  return(DF)
}