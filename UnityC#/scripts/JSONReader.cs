using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class JSONReader {

    static private DataSet points;

    private string file;

    static public List<DataObject> getData(string file)
    {
        //Read(file);
        //Debug.Log(points);
        return points.points;
    }

    static public void Read(string file)
    {
        string path = Path.GetFullPath(Path.Combine(Application.streamingAssetsPath, file));
        Debug.Log(path);

        if (File.Exists(path))
        {
            string json = File.ReadAllText(path);
            Debug.Log(json);
            points = JsonUtility.FromJson<DataSet>(json);
        }
        else
        {
            Debug.Log("File not found");
        }
    }

}


