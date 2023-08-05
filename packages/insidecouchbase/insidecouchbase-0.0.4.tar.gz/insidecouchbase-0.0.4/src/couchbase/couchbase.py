import requests
import telnetlib
import sys
from tabulate import tabulate
import pandas as pd

class couchbasePlatform:
    def __init__(self,hostName,loginInformation,loginSecret):
        self.hostname=hostName
        self.logininformation=loginInformation
        self.loginsecret=loginSecret
        self.clusterDefinition=''

    def getClusterVersion(self):
        try:
            urlForHealth = f"http://{self.hostname}:8091/pools"
            #print(self.hostname)
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            self.clusterVersion=resultParsed['implementationVersion']
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    def getNodesOnCluster(self):
        try:
            urlForHealth = f"http://{self.hostname}:8091/pools/nodes"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            nodes=resultParsed.get('nodes')
            nodeList=[]
            for node in nodes:
                #print(node)
                clusterMember=node.get('clusterMembership')
                healtStatus=node.get('status')
                nodeIp=node.get('hostname')
                services=node.get('services')
                version=node.get('version')
                nodeModel={
                    "nodeIP": nodeIp,
                    "clusterMember":clusterMember,
                    "healtStatus": healtStatus,
                    "services" : services,
                    "couchbaseVersion":version
                }
                nodeList.append(nodeModel)
                self.clusterNodes=nodeList
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    def getUsersOnCluster(self):
        try:
            urlForHealth = f"http://{self.hostname}:8091/settings/rbac/users"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            userList=[]
            for user in resultParsed:
                userModel={
                    "userName": user.get('name'),
                    "userRole": user.get('roles')
                }
                userList.append(userModel)
            self.usersOnCluster=userList
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    def getClusterName(self):
        try:
            urlForHealth = f"http://{self.hostname}:8091/pools/nodes"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            self.clusterDefinition=resultParsed['clusterName']
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    def getRebalance(self):
        try:
            urlForHealth = f"http://{self.hostname}:8091/pools/default/pendingRetryRebalance"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            #print(resultParsed)
            self.rebalanceStatus=resultParsed
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    def getXdcrConnections(self):
        try:
            urlForHealth = f"http://{self.hostname}:8091/pools/default/remoteClusters"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            xdcrConnections=[]
            for remote in resultParsed:
                xdcrModel={
                    "xdcrName": remote.get('name'),
                    "xdcrConnectivity": remote.get('connectivityStatus'),
                    "targetNode":remote.get('hostname').split(":")[0]
                }
                xdcrConnections.append(xdcrModel)
            self.xdcrConnections=xdcrConnections
        except Exception as couchbaseBucketException:
            return couchbaseBucketException
    def prepareBucketData(self):
        try:
            bucketDetailReport=[]
            bucketsEndpoint = f"http://{self.hostname}:8091/pools/default/buckets"
            getBucketDetails = requests.get(
                url=bucketsEndpoint, auth=(self.logininformation,self.loginsecret))
            overallBucketData = getBucketDetails.json()
            bucketList=[]
            for bucket in overallBucketData:
                bucketList.append(bucket.get('name'))
                bucketName=bucket.get('name')
                vbucketMap=bucket.get('vBucketServerMap')
                vbucketCount=vbucketMap.get('vBucketMap')
                count=0
                for vbucket in vbucketCount:
                    count=count+1
                # call bucket endpoint with name and collect result
                bucketSpecialPoint = f"http://{self.hostname}:8091/pools/default/buckets/{bucketName}/stats"
                detailedBucket = requests.get(
                    url=bucketSpecialPoint, auth=(self.logininformation,self.loginsecret))
                statReport = detailedBucket.json()
                # collect details
                bucketStats=bucket.get('basicStats')
                avgResident = sum(statReport['op']['samples']['vb_active_resident_items_ratio'])/len(
                            statReport['op']['samples']['vb_active_resident_items_ratio'])
                bucketRecord = {
                    "bucketName": bucketName,
                    "primaryVbucketCount": count,
                    "bucketType": bucket.get('bucketType'),
                    "bucketReplicas": bucket.get('vBucketServerMap').get('numReplicas'),
                    "bucketQuotaPercentage": round(bucketStats.get('quotaPercentUsed'), 1),
                    "bucketItemCount":  round(bucketStats.get('itemCount')),
                    "bucketResidentRatio": avgResident,
                    "bucketDisUsedInMb": round((bucketStats.get("diskUsed"))/1024/1024, 1)
                }
                bucketDetailReport.append(bucketRecord)
            self.buckets=bucketDetailReport
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    def prepareIndexData(self):
        try:
            indexEndpoint = f"http://{self.hostname}:9102/api/v1/stats?skipEmpty=true&redact=true&pretty=true"
            getIndexDetails = requests.get(
                url=indexEndpoint, auth=(self.logininformation, self.loginsecret))
            overallIndexData = getIndexDetails.json()
            indexList = []
            for index in overallIndexData:
                indexData=overallIndexData[index]
                indexName=index
                indexItemSize=indexData.get('avg_item_size')
                indexItemCount=indexData.get('items_count')
                indexHitPercent=indexData.get('cache_hit_percent')
                indexResidentPercent=indexData.get('resident_percent')
                indexIBuildPercent=indexData.get('initial_build_progress')
                indexRecord={
                    "indexName": indexName,
                    "indexAverageItemSize": indexItemSize,
                    "indexItemCount": indexItemCount,
                    "indexHitPercent": indexHitPercent,
                    "indexResidentPercent": indexResidentPercent,
                    "indexBuildPercent": indexIBuildPercent
                }
                indexList.append(indexRecord)
            self.indexes=indexList
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    

    def getSettings(self):
        try:
            urlForHealth = f"http://{self.hostname}:8091/settings/autoFailover"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            settingsArray=[]
            settingModel={
                "configName": 'autofailover',
                "status": resultParsed.get('enabled'),
            }
            settingsArray.append(settingModel)
            urlForHealth = f"http://{self.hostname}:8091/settings/alerts"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            settingModel={
                "configName": 'email-alerting',
                "status": resultParsed.get('enabled'),
            }
            settingsArray.append(settingModel)
            urlForHealth = f"http://{self.hostname}:8091/settings/autoCompaction"
            getNodeDetails = requests.get(
                url=urlForHealth, auth=(self.logininformation, self.loginsecret))
            resultParsed = getNodeDetails.json()
            settingModel={
                "configName": 'auto-compaction',
                "status": resultParsed.get('autoCompactionSettings').get('databaseFragmentationThreshold').get('percentage')
            }
            settingsArray.append(settingModel)
            self.settingsCluster=settingsArray
        except Exception as couchbaseBucketException:
            print(couchbaseBucketException)
    def takePicture(self):
        clusterNodes=self.clusterNodes
        clusterBuckets=self.buckets
        clusterRoles=self.usersOnCluster
        clusterSettings=self.settingsCluster
        clusterXdcr=self.xdcrConnections
        dataFrameforNodes=pd.DataFrame(clusterNodes)
        dataFrameforBuckets=pd.DataFrame(clusterBuckets)
        dataFrameforRoles=pd.DataFrame(clusterRoles)
        dataFrameforXdcr=pd.DataFrame(clusterXdcr)
        dataFrameFailover=pd.DataFrame(clusterSettings)
        print("----- Cluster Nodes -----")
        print(tabulate(dataFrameforNodes, headers = 'keys', tablefmt = 'psql'))
        print("----- Cluster Buckets -----")
        print(tabulate(dataFrameforBuckets, headers = 'keys', tablefmt = 'psql'))
        print("----- Cluster XDCR -----")
        print(tabulate(dataFrameforXdcr, headers = 'keys', tablefmt = 'psql'))
        print("----- Cluster Roles -----")
        print(tabulate(dataFrameforRoles, headers = 'keys', tablefmt = 'psql'))
        print("----- Cluster Settings -----")
        print(tabulate(dataFrameFailover, headers = 'keys', tablefmt = 'psql'))
        checkResults=[]
        nodeVersions=[]
        for node in clusterNodes:
            healtStatus=node.get('healtStatus')
            clusterMember=node.get('clusterMember')
            nodeVersion=node.get('couchbaseVersion')
            nodeVersions.append(nodeVersion)
            mdsControlCount=len(node.get('services'))
            if healtStatus!='healthy' or clusterMember!='active':
                checkModel={
                    "problemStatement": 'Node is not available or joined cluster.',
                    "problemArea": node.get('nodeIP'),
                    "problemSeverity": 'Critical'
                }
                checkResults.append(checkModel)
            else:
                pass
            if mdsControlCount > 1:
                checkModel={
                    "problemStatement": 'The node has multiple couchbase services.For production MDS model should be followed.',
                    "problemArea": node.get('nodeIP'),
                    "problemSeverity": 'Medium'
                }
                checkResults.append(checkModel)
        for bucket in clusterBuckets:
            bucketReplica=bucket.get('bucketReplicas')
            vbucketCount=bucket.get('primaryVbucketCount')
            bucketResident=bucket.get('bucketResidentRatio')
            if bucketReplica==0:
                checkModel={
                    "problemStatement": f''' {bucket.get('bucketName')} has no replica configured''',
                    "problemArea": 'Bucket',
                    "problemSeverity": 'Critical'
                }
                checkResults.append(checkModel)
            elif bucketReplica==3:
                checkModel={
                    "problemStatement": f''' {bucket.get('bucketName')} has 3 replica configured''',
                    "problemArea": 'Bucket',
                    "problemSeverity": 'Warming'
                }
                checkResults.append(checkModel)
            if vbucketCount%1024!=0:
                checkModel={
                    "problemStatement": f''' {bucket.get('bucketName')} has missing primary vbucket''',
                    "problemArea": 'Bucket',
                    "problemSeverity": 'Critical'
                }
                checkResults.append(checkModel)
            if bucketResident < 10:
                checkModel={
                    "problemStatement": f''' {bucket.get('bucketName')} has low resident ratio''',
                    "problemArea": 'Bucket',
                    "problemSeverity": 'Critical'
                }
                checkResults.append(checkModel)
        dataFrameResults=pd.DataFrame(checkResults)
        print("----- Check Notes -----")
        print(tabulate(dataFrameResults, headers = 'keys', tablefmt = 'psql'))
        return f''' Finished healtcheck.'''