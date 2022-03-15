# Contributing

- JupyterHub
  - [Settings](https://settings-fall.rcnyu.org/)
  - [Instructor site](https://padmgp-4506-spring-instructor.rcnyu.org/)

## Loading the notebooks locally

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
1. Create the environment:

   ```sh
   conda env create -f extras/environment.yml
   ```

1. Activate the environment:

   ```sh
   conda activate python-public-policy
   ```

1. Start the Jupyter server:

   ```sh
   jupyter notebook
   ```

## Slides

While the lecture notes can be viewed as a plain notebook, they are also [visible as slides](https://rise.readthedocs.io/en/stable/usage.html#running-a-slideshow).

## Notebook cleanup

To ensure that notebooks have the correct execution order and output, run them non-interactively.

```sh
./extras/scripts/update.sh <file>.ipynb
```

## Start of class checklist

- Zoom
  1. Start meeting
  1. Sign into Zoom Classroom
  1. `Switch Camera` to `Logi Rally Camera`
  1. Mute mic and speakers on computer
  1. Unmute mic on Zoom Classroom
  1. Start recording
- [Set placeholders](https://settings-fall.rcnyu.org/)
- Open [participation spreadsheet](https://docs.google.com/spreadsheets/d/19y3cXYYC-3KLGn6ay0GJ6Bt_LN_AXdxdhf4b3qPnUjE/edit#gid=773327)
  - If first couple classes: take attendance for recording [Academic Engagement](https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/faculty/academic-engagement.html)

## Assignment checks

The following should be true for each assignment:

- Links to the [instructions to submit](README.md#turning-in-assignments)
- `Add honor Pledge` box for each is unchecked
- Dates are correct:
  - `Open Date`s are Thursdays at 6:45pm ET, week by week
  - `Due Date`s should match the [schedule](syllabus.md#schedule): subsequent Thursdays 6:45pm, week by week
  - `Accept Until` date should be the Sundays at 6:45pm following the `Due Date`
    - Exceptions is HW6, which can't be turned in late
  - `Resubmission Accept Until` should be the Thursday at 6:45pm following the `Due Date`
    - Exception is HW6, which doesn't allow resubmission
- Associated with the `Homework` `gradebook category`
- Each Assignment has been Posted

## Homework extensions

1. Go to [Assignments](https://brightspace.nyu.edu/d2l/lms/dropbox/admin/folders_manage.d2l?ou=156784)
1. Edit Assignment
1. Expand "Availability Dates & Conditions"
1. Click "Manage Special Access"
1. Check "Has Due Date"

## Data sets

Canonical copies of data are in [a Google Drive folder](https://drive.google.com/drive/folders/1oCKV6NfvGO007aynTmSSbr1kzqXi4dHV), synced locally with [Google Drive for desktop](https://support.google.com/a/users/answer/9965580). Data is then compressed and uploaded to [a Google Cloud Storage bucket](https://console.cloud.google.com/storage/browser/python-public-policy/data) via [Terraform](terraform/). [Descriptions of the data sets.](terraform/data.tf)
