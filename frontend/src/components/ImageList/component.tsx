import { Button, ImageList as MuiImageList, ImageListItem, ImageListItemBar } from '@mui/material';
import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '@/providers/UserProvider';
import { Image } from '@/types';
import { authorizedFetch, authorizedFetchPostFile } from '@/utils/fetch';
import {
  buildImageDetailUrl,
  buildImageListFilterLocationlUrl,
  buildImageListUrl,
} from '@/utils/utils';
import PaperDefault from '@components/PaperDefault';
import { useParams } from 'react-router-dom';
import Typography from '@mui/material/Typography';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { styled } from '@mui/material/styles';
import { enqueueSnackbar } from 'notistack';
import Grid from '@mui/material/Grid';
import dayjs from 'dayjs';
import { DATE_FORMAT } from '@/utils/constants';

const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

const DivMargin = styled('div')({
  marginTop: '32px',
});

const ImageList = () => {
  const { id } = useParams();
  const { dispatch } = useContext(AuthContext);
  const [imageList, setImageList] = useState<Image[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await authorizedFetch(dispatch, buildImageListFilterLocationlUrl(id ?? ''));
      const data = await res.json();
      if (res.status === 200) {
        setImageList(data);
      }
    };
    fetchData();
  }, [dispatch, id]);

  const imageDelete = async (id: number) => {
    const res = await authorizedFetch(dispatch, buildImageDetailUrl(id), 'DELETE');
    if (res.status === 204) {
      enqueueSnackbar(`Image deleted`, {
        variant: 'success',
      });
    }
    setImageList(imageList.filter((item) => item.id !== id));
  };

  const uploadImage = async (fileList: FileList | null) => {
    const file = fileList?.item(0);
    if (fileList !== null && file instanceof File && id !== undefined) {
      const formData = new FormData();
      formData.append('location', id);
      formData.append('image', file);

      const res = await authorizedFetchPostFile(dispatch, buildImageListUrl, formData);
      if (res.status === 201) {
        enqueueSnackbar(`Image uploaded`, {
          variant: 'success',
        });
        const data = await res.json();
        setImageList([...imageList, data]);
      } else {
        enqueueSnackbar(`Image not uploaded`, {
          variant: 'error',
        });
      }
    }
  };

  return (
    <DivMargin>
      <PaperDefault>
        <Typography variant="h5">Images</Typography>
        <MuiImageList>
          {imageList.map((item) => (
            <ImageListItem key={item.image}>
              <img srcSet={item.image} src={item.image} loading="lazy" alt="" />
              <Grid container sx={{ marginTop: '10px' }}>
                <Grid item xs={6}>
                  <div>
                    Created: {item.uploadDate ? dayjs(item.uploadDate).format(DATE_FORMAT) : '–'}
                  </div>
                  <div>Uploader: {item.uploader ? item.uploader : '–'}</div>
                  <div>Description: {item.description}</div>
                  <div>
                    Height: {item.height} Width: {item.width}
                  </div>
                </Grid>
                <Grid container item xs={6} justifyContent="flex-end">
                  <Grid item>
                    <Button
                      variant="contained"
                      color="error"
                      name="delete"
                      onClick={() => imageDelete(item.id)}
                    >
                      Delete
                    </Button>
                  </Grid>
                </Grid>
              </Grid>
            </ImageListItem>
          ))}
        </MuiImageList>
        <Grid container justifyContent="center">
          <Grid item>
            <Button
              component="label"
              variant="contained"
              tabIndex={-1}
              startIcon={<CloudUploadIcon />}
            >
              Upload image
              <VisuallyHiddenInput
                type="file"
                onChange={(event) => uploadImage(event.target.files)}
                multiple
              />
            </Button>
          </Grid>
        </Grid>
      </PaperDefault>
    </DivMargin>
  );
};

export default ImageList;
