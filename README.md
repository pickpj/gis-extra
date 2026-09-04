# gis-extra  
  
---  

### map-marker  
An interactive map tool to create/edit geodataframes. The shapes are paired with editable metadata. The intention was so one can systematically comb through streetview imagery. Or for collecting/identifying areas with out-dated imagery to review/survey later. Fairly niche. Running iD editor locally might be a better option.  
  
---  
### osmiumupdate  
A simple python script to download and apply change files using osmium. Downloads from geofabrik, uses wget & osmium, and sends notifications on linux through echo text > /dev/pts/0.  
  
---  
### flood-routing
After processing a DEM with DDM Hydrologic. The exported flowpath(strahler) and catchment information can be used to map out points where a road may flood. The python notebook has an interactive ipyleaflet map with widgets to adjust the parameters. This information can then be "compiled" into the pbf road data (ie cut up the roads) for use in other applications (such as routing through osmand).  
The ipyleaflet interactive map:  
<img width="1156" height="760" alt="flood routing sim" src="https://github.com/user-attachments/assets/8304ed41-4dc6-45df-82f4-711b9e6865b1" />  
  
---  
