package org.example.backend;

import org.example.backend.repository.AddressRepository;
import org.example.backend.repository.AnnouncementRepository;
import org.example.backend.repository.CategoryRepository;
import org.example.backend.repository.EventCategoryRepository;
import org.example.backend.repository.EventRepository;
import org.example.backend.repository.EventServiceRepository;
import org.example.backend.repository.OrganizerRepository;
import org.example.backend.repository.RegistrationRepository;
import org.example.backend.repository.ReviewRepository;
import org.example.backend.repository.ServiceRepository;
import org.example.backend.repository.SpatialRefSysRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;

public class BaseTest {

    @Autowired
    private AddressRepository addressRepository;

    @Autowired
    private AnnouncementRepository announcementRepository;

    @Autowired
    private CategoryRepository categoryRepository;

    @Autowired
    private EventCategoryRepository eventCategoryRepository;

    @Autowired
    private EventRepository eventRepository;

    @Autowired
    private EventServiceRepository eventServiceRepository;

    @Autowired
    private OrganizerRepository organizerRepository;

    @Autowired
    private RegistrationRepository registrationRepository;

    @Autowired
    private ReviewRepository reviewRepository;

    @Autowired
    private ServiceRepository serviceRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private SpatialRefSysRepository spatialRefSysRepository;



}
