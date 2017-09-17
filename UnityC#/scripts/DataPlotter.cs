using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;


// using System.Net.Http;

[System.Serializable]
public class DataPlotter : MonoBehaviour {

    public GameObject PointMaker;
    public string inputfile;
    public string json;

    private List<DataObject> points = new List<DataObject>();

	// Use this for initialization
	void Start () {

        DontDestroyOnLoad(gameObject);
        // postRequest(pointList);
        UnityHTTP.Request someRequest = new UnityHTTP.Request("get", "http://127.0.0.1:8080/data?location=all&service=Ambulance%20(Emergency)&date_range=0&AxisX=number_of_providers&AxisY=number_of_fee_for_service_beneficiaries&AxisZ=average_number_of_users_per_provider");
        someRequest.Send((request) =>
        {
            // parse some JSON, for example:

            json = request.response.Text.Replace(@"\", string.Empty);
            json = json.Substring(2, json.Length - 5);
            json = "{\"points\":[" + json + "]}";
            Debug.Log(json);
            points = JsonUtility.FromJson<DataSet>(json).points;
            Debug.Log(points.Count);

            
        });


        StartCoroutine(PlotPoints());
    }



    IEnumerator PlotPoints() {
        yield return new WaitForSeconds(20f);
        Debug.Log("before loop");
        Debug.Log(points.Count);
        for (int i = 0; i < points.Count; i++)
        {
            Debug.Log("During Loop");
            float x = System.Convert.ToSingle(points[i].number_of_providers);
            float y = System.Convert.ToSingle(points[i].number_of_fee_for_service_beneficiaries);
            float z = System.Convert.ToSingle(points[i].average_number_of_users_per_provider);
            Instantiate(PointMaker, new Vector3(x, y/10000, z), Quaternion.identity);
            yield return new WaitForEndOfFrame();

        }
        Debug.Log("After Loop");

        Debug.Log(points);
        //Instantiate(PointMaker, new Vector3(1, 1, 1), Quaternion.identity);

        //foreach (DataObject o in points)
    }

    public IEnumerator postRequest(DataObject[] pointList)
    {
        Debug.Log("In PostRequest");
        UnityHTTP.Request request = new UnityHTTP.Request("get", "http://127.0.0.1:8080/data?location=all&service=Ambulance%20(Emergency)&date_range=0&AxisX=number_of_providers&AxisY=number_of_fee_for_service_beneficiaries&AxisZ=average_number_of_users_per_provider");
        request.Send();
        Debug.Log("entering While");
        while (!request.isDone)
        {
            int i = 0;
            if( i%10 == 0)
            {
                Debug.Log("still in while" + i);
            }
            yield return null;
            i++;
        }

        //JSON thing = new JSON(request.response.Text);
        Debug.Log(request.response.Text);
    }



}
