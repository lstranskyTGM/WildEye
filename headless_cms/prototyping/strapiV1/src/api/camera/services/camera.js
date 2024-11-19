'use strict';

/**
 * camera service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::camera.camera');
