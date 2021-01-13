import express from 'express';
import getMD from '../controllers/md';
const router = express.Router();
import getMS from '../controllers/ms';
import getMX from '../controllers/mx';
import getWD from '../controllers/wd';
import getWS from '../controllers/ws';

router.get('/ms', getMS);
router.get('/md', getMD);
router.get('/ws', getWS);
router.get('/wd', getWD);
router.get('/mx', getMX);

export = router;
