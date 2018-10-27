# awk -F"~" -f csv2json.awk > internal_companies.json
#[{"model": "web.company", "pk": 1, "fields": {"company_name": "google"}}]
BEGIN{
  print "["
}
{
  print "{"
    print "\"model\": \"web.company\","
    print "\"pk\":",NR+1000,","
    print "\"fields\":{"
      print "\"company_name\": \""$1"\""
    print "}"
    print "},"
}
END{
  print "]"
}

