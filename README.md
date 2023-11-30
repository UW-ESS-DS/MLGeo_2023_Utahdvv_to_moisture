## Repo-name: MLGeo_2023_Utahdvv_to_moisture <br />
### Project Purpose
Exploring hydrological variables from seismology aspects

### Background / Scientific Motivation
The impacts of Climate change and city expansion on water resources have been non-ignorable in recent decades. The most direct measurement of water resources is groundwater (or reservoirs and lakes water levels). Conventionally, monitoring groundwater levels, whether in aquifers or as soil moisture, requires in-situ instrumentation with low spatial resolution or remote sensing with low temporal resolution (e.g., GRACE data, Landerer and Swenson, 2012). From the seismology aspect, a proper seismic measurement, called seismic velocity change (dv/v),  has been used to explore near-surface hydrological observation on a relatively small scale, such as a few kilometers. Several research studies (Lecocq et al., 2017; Clements and Denolle, 2018, 2023; Illien et al., 2021; Mao et al., 2022) have successfully explored the anti-correlation relationship between seismic velocity changes and near-surface hydrological variables (i.e., groundwater table variations, soil moisture, etc.). While a good anti-correlation between seismic velocity changes and near-surface hydrological variables was revealed, there are some other potential factors, such as temperature, that also contributed to the variations in seismic velocity changes and hydrological variables (Richter et al., 2014; Lecocq et al., 2017; Clements and Denolle, 2023) and need to be taken into account in this relation. However, these studies explore the relationship between the terms with a linear function. In this repo, we consider this relation a non-linear problem and would like to try using ML algorithms to resolve this problem.

### Research Question 
- What are the primary impact factors on near-surface hydrological resources? 
- How does a non-linear problem help resolve near-surface hydrological resources monitoring?
- Can we further predict near-surface hydrological variables based on seismic and temperature measurements? 

### Datasets
The seismic measurements are the seismic velocity changes from Feng et al. (_in prep_). The soil moisture equivalent water thickness (EWT) data is from the North American Land Data Assimilation System project phase 2 (NLDAS-2; Xia et al., 2012ab; NLDAS phase-2, 2022). The temperature data is from the Parameter-elevation Relationships on Independent Slopes Model (PRISM) Gridded Climate Data (PRISM Climate Group, 2023).  <br />
All these data above have been compiled as .csv files according to station locations.

### ML Method
Neural Network

### Model Training 
TBD.

### Reproducibility
TBD.

### References
- Clements, T., & Denolle, M. A. (2018). Tracking groundwater levels using the ambient seismic field. Geophysical Research Letters, 45(13), 6459-6465. https://doi.org/10.1029/2018GL077706  <br />
- Clements, T., & Denolle, M. A. (2023). The Seismic Signature of California's Earthquakes, Droughts, and Floods. Journal of Geophysical Research: Solid Earth, 128(1), e2022JB025553. https://doi.org/10.1029/2022JB025553  <br />
- Feng et al. (in prep) A decadal survey of the near-surface seismic velocity response to hydrological variations in Utah, United States.  <br />
- Illien, L., Andermann, C., Sens‐Schönfelder, C., Cook, K. L., Baidya, K. P., Adhikari, L. B., & Hovius, N. (2021). Subsurface moisture regulates Himalayan groundwater storage and discharge. AGU Advances, 2(2), e2021AV000398. https://doi.org/10.1029/2021AV000398  <br />
- Landerer, F. W., & Swenson, S. C. (2012). Accuracy of scaled GRACE terrestrial water storage estimates. Water resources research, 48(4). https://doi.org/10.1029/2011WR011453
- Lecocq, T., Longuevergne, L., Pedersen, H. A., Brenguier, F., & Stammler, K. (2017). Monitoring ground water storage at mesoscale using seismic noise: 30 years of continuous observation and thermo-elastic and hydrological modeling. Scientific reports, 7(1), 14241. https://doi.org/10.1038/s41598-017-14468-9  <br />
- Mao, S., Lecointre, A., van der Hilst, R. D., & Campillo, M. (2022). Space-time monitoring of groundwater fluctuations with passive seismic interferometry. Nature communications, 13(1), 4643.  https://doi.org/10.1038/s41467-022-32194-3 <br />
- PRISM Climate Group, Oregon State University, https://prism.oregonstate.edu, data created 1 Jan 2006, accessed Jan 2023. <br />
- Richter, T., Sens‐Schönfelder, C., Kind, R., & Asch, G. (2014). Comprehensive observation and modeling of earthquake and temperature‐related seismic velocity changes in northern Chile with passive image interferometry. Journal of Geophysical Research: Solid Earth, 119(6), 4747-4765. https://doi.org/10.1002/2013JB010695  <br />
- Xia et al. (2012a). Continental‐scale water and energy flux analysis and validation for North American Land Data Assimilation System project phase 2 (NLDAS‐2): 2. Validation of model‐simulated streamflow. Journal of Geophysical Research: Atmospheres, 117(D3).  <br />
- Xia et al. (2012b). Continental‐scale water and energy flux analysis and validation for the North American Land Data Assimilation System project phase 2 (NLDAS‐2): 1. Intercomparison and application of model products. Journal of Geophysical Research: Atmospheres, 117(D3).  <br />
