import json
import os
import logging
import html_scrape_play as blog2text_funcs
import asyncio

# 3rd party imports
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
BUCKET_NAME = "blog2ptt-bucket"


def upload_file_to_s3(file_name: str, bucket: str, object_name: str) -> bool:
    """
    Purpose:
        Uploads a file to s3
    Args/Requests:
         file_name: name of file
         bucket: s3 bucket name
         object_name: s3 name of object
    Return:
        Status: True if uploaded, False if failure
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    try:

        response = s3.upload_file(file_name, bucket, object_name)
        # logging.info(response)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def lambda_entry_point(event, context):
    """
    Purpose:
        Runs lambda function async
    Args/Requests:
         event: event
         context: context
    Return:
        http json response
    """
    return asyncio.run(convert_blog_2_ppt(event,context))


async def convert_blog_2_ppt(event, context):
    """
    Purpose:
        Converts blog post to ppt
    Args/Requests:
         event: event
         context: context
    Return:
        http json response
    """
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
    }
    print("This is the main event")
    print(event)

    try:

        if "body" in event:
            curr_data = json.loads(event["body"])

            if "blog_url" in curr_data:
                blog_url = curr_data["blog_url"]
                print("Got url from event!!!")
            else:
                print("No url...")
                body["status"] = "blog_url param is empty"
                response = {"statusCode": 200, "body": json.dumps(body)}
                return response

        else:
            print("No blog url, using deafult")
            blog_url = "https://dev.to/banjtheman/dc-fire-and-ems-data-visualizer-4a6l"
        
        ppt_name = f"{blog_url.split('/')[-1]}.pptx"
        ppt_loc = f"/tmp/ppts/{ppt_name}"
        print(f"Converting blog {blog_url} to ppt")

        blog_sections, num_sections = blog2text_funcs.get_html_sections(blog_url)

        ppt = await blog2text_funcs.convert_sections_to_ppt(blog_sections, num_sections)
        # Just to be safe
        os.system("mkdir -p /tmp/ppts/")
        ppt.save(ppt_loc)

        # TODO return binary data?
        body["status"] = "good"

        # Bah upload to s3
        print("Uploading to s3")
        upload_file_to_s3(ppt_loc,BUCKET_NAME,ppt_name)
        s3_url = f"https://blog2ptt-bucket.s3.amazonaws.com/{ppt_name}"
        print(f"s3 url: {s3_url}")

        body["powerpoint_url"] = s3_url
        response = {"statusCode": 200, "body": json.dumps(body)}

        print("done and done")

    except Exception as error:
        logging.error(error)
        body["status"] = "big error"
        response = {"statusCode": 500, "body": json.dumps(body)}


    return response


async def main():
    print("Go!")
    blog_url = (
        "https://dev.to/banjtheman/dc-fire-and-ems-data-visualizer-4a6l"
    )

    print(f"Converting blog {blog_url} to ppt")

    blog_sections, num_sections = blog2text_funcs.get_html_sections(blog_url)
    # utils.save_json("example.json", blog_sections)

    # utils.write_to_file("example.html", html_text)

    ppt = await blog2text_funcs.convert_sections_to_ppt(blog_sections, num_sections)
    ppt.save("tmp/ppts/end_to_end.pptx")

    print("done and done")


if __name__ == "__main__":
    asyncio.run(main())
    # main()
