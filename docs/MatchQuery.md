# MatchQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The text/numeric/date to query for. | 
**operator** | **str** | The operator flag can be set to or or and to control the boolean clauses (defaults to or). | [optional] 
**minimum_should_match** | **int** | The minimum number of optional should clauses to match. | [optional] 
**analyzer** | **str** | The analyzer that will be used to perform the analysis process on the text. Defaults to the analyzer that was used to index the field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


